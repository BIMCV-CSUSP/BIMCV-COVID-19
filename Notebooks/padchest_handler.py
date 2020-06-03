import pandas as pd
import ast
import imageio
import matplotlib.pyplot as plt
import os
import numpy as np
import h5py
import cv2
from skimage.transform import resize
import ast


class PadChestDataHandler:

    def __init__(self, nb_elements=10, start_idx = 0, end_idx = None,
                 shuffle = False, augment=False, image_size=(299,299), 
                 nchannels = 1, normalize=True,
                 tree_file = '/mnt/ssd/tree_term_CUI_counts_160K_mod.csv',
                 h5_file = '/mnt/ssd/padchest_pa_1024.hdf5',
                 df_file =  '/mnt/ssd/padchest_pa_1024_rs.csv',
                 augmentation_coefficients=[15,15,5,10]):
        
        # Management of the dataframe
        self.df_file = df_file

        # In the reference standard file there are images from the same subject at the beginning and at the enc
        # this biases the results - we need to order them to group the images of the same subject, so that the 
        # same subject does not appear in training, test and validation
        dtt = pd.read_csv(self.df_file, low_memory=False)
        
        if not 'h5_idx' in dtt.columns:
            dtt_idx = range(0, len(dtt))
            dtt['h5_idx'] = dtt_idx
        else:
            # This is for the covid19 dataset
            dtt = dtt[ (dtt['Position_Manual']=='PA') &
                     ( (dtt['Modality']=='CR') |
                       (dtt['Modality']=='DX')
                     )]
            
        dtt = dtt.sort_values(by='PatientID')
        self.rs = dtt
        self.__parse_strings_into_lists_in_reference_standard()
        
        # Management of the hierarchy and generation of str_to_idx and idx_to_str
        self.tree_file = tree_file
        self.__generate_parents_and_childs()
        
        # Image handling
        self.h5_file = h5_file
        self.dt = h5py.File(self.h5_file, 'r')
        self.imgs = self.dt['images']     
        self.image_size = image_size
        self.nchannels = nchannels
        self.idxs_batch = None
        self.normalize = normalize
        self.augment = augment
        self.augmentation_coefficients = augmentation_coefficients
        self.nb_elements = nb_elements
        self.end_idx = end_idx
        self.start_idx = start_idx
        if self.end_idx is None or self.end_idx < self.start_idx:
            self.end_idx = len(self.rs)
        self.size =  self.end_idx - self.start_idx
#         print(self.size)
#         print(int(self.size / self.nb_elements) + int(self.size % self.nb_elements > 0))
        
        self.shuffle = shuffle
        self.idxs = self.__idxs_gen()


    def __idxs_gen(self):
        tmp_idxs = list(range(self.start_idx, self.end_idx))
        if self.shuffle:
            np.random.shuffle(tmp_idxs)
        return tmp_idxs


    def __augment_image(self, image):
        tx = np.random.randn()*self.augmentation_coefficients[0]
        ty = np.random.randn()*self.augmentation_coefficients[1]
        angle = np.random.randn()*self.augmentation_coefficients[2]
        zoom = 1 + np.random.randn()/self.augmentation_coefficients[3]

        (h, w) = image.shape
        (cX, cY) = (w // 2, h // 2)

        # Matrix for the zoom operation (in the center)
        Mz = np.eye(3)
        Mz[0,0] = zoom
        Mz[1,1] = zoom
        Mz[0,2] = (h-zoom*h)/2
        Mz[1,2] = (w-zoom*w)/2

        # Matrix for the rotation
        Mr = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
        Mr3 = np.eye(3)
        Mr3[0:2,:] = Mr

        # Matrix for the translation
        Mt = np.eye(3)
        Mt[0,2] = tx
        Mt[1,2] = ty

        # Combines the three matrices
        Mrt = np.matmul(Mz, Mr3)
        Mrt = np.matmul(Mrt, Mt)

        imr = cv2.warpAffine(image, Mrt[0:2,:], (image.shape[0], image.shape[1]))
        return imr    
        

    def __parse_strings_into_lists_in_reference_standard(self):
        # al = []
        diags = []
        locs = []
        # al_locs = []

        for x in self.rs['Labels']:
            if not isinstance(x, str):
                diags.append('')
            else:
                r = ast.literal_eval(x)
                rn = [n.strip() for n in r]
                diags.append(rn)
                # al.extend(rn)
                
        for x in self.rs['Localizations']:
            if not isinstance(x, str):
                locs.append('')   
            else:
                r = ast.literal_eval(x)
                rn = [n.strip() for n in r]
                locs.append(rn)
                # al_locs.extend(rn)
 
        self.rs['Diagnosis'] = diags
        self.rs['Locs'] = locs


    def __generate_parents_and_childs(self):
        r = open(self.tree_file,'r')
        parents = dict()
        parent = []
        curr_depth = 0
        last_node = None
        for l in r.readlines():
            lc = l.replace("\\",'').replace("\n", "").replace("─", " ").replace("├"," ").replace("│"," ").replace("└", " ")
            spaces = len(lc) - len(lc.lstrip())
            level = int(spaces/4)
            if level > curr_depth:
                parent.append(last_node)
            if level < curr_depth:
                for i in range(level, curr_depth):
                    parent.pop()
            curr_depth = level
            last_node = lc.split("[")[0].strip()
            if 'localization' in parent:
                last_node = 'loc ' + last_node
            parents[last_node] = parent.copy()
            # print("%02i: - %s (%s) ; parent: %s" % (level, lc.split("[")[0], last_node, parent))
        childs = dict()
        for k in parents.keys():
            child_list = []
            for k2 in parents.keys():
                if k in parents[k2]:
                    child_list.append(k2)
            childs[k] = child_list   
        self.parents = parents
        self.childs = childs

        str_to_idx = dict()
        idx_to_str = dict()
        for i,k in enumerate(parents.keys()):
            str_to_idx[k] = i
            idx_to_str[i] = k
        self.str_to_idx = str_to_idx
        self.idx_to_str = idx_to_str
        self.y_dimension = len(self.str_to_idx)

    def steps_per_epoch(self):
        return int(self.size / self.nb_elements) + int(self.size % self.nb_elements > 0)

    def get_sample(self):
        nb_idxs = []
        if self.nb_elements <= len(self.idxs):
            for n in range(self.nb_elements):
                nb_idxs.append(self.idxs.pop(0))
            if len(self.idxs) == 0:
                self.idxs = self.__idxs_gen()
        else:
            nb_idxs = np.array(self.idxs)
            self.idxs = self.__idxs_gen()

        self.idxs_batch = nb_idxs
            
        x = np.zeros((len(nb_idxs), self.image_size[0],self.image_size[1], self.nchannels), dtype=np.float32)
        y = np.zeros((len(nb_idxs), self.y_dimension))

        for ix in range(len(nb_idxs)):
            im = self.imgs[self.rs.iloc[nb_idxs[ix]].h5_idx].copy()
            
            if (im.shape[0] != self.image_size[0]) or (im.shape[1] != self.image_size[1]):
                imr = resize(im, (self.image_size[0], self.image_size[1]), 
                                  anti_aliasing=True,  preserve_range=True)            
            else:
                imr = im
            if self.augment:
                imt = self.__augment_image(imr)
            else:
                imt = imr
            if self.normalize:
                std = np.std(np.ravel(imt))
                if std != 0:
                    imt = (imt*1.0 - np.mean(np.ravel(imt)))/np.std(np.ravel(imt))

            for kk in range(0, self.nchannels):
                x[ix, :, :, kk] = imt

            # Turns the diagnosis and locations into the indexes of the reference
            idxs = self.labels_to_indexes(self.rs.iloc[nb_idxs[ix]].Diagnosis + self.rs.iloc[nb_idxs[ix]].Locs)
            for i in idxs:
                y[ix,i] = 1
        return x, y.astype(np.int16)

    def gen_batch(self):
        while 1:
            x, y = self.get_sample()
            yield (x, y)

    def labels_to_indexes(self, labels):
        all_labels = []
        for k in labels:
            if k == '':
                continue
            all_labels.extend([k])
            all_labels.extend(self.parents[k])
        all_labels = list(set(all_labels))
        idxs = [self.str_to_idx[k] for k in all_labels]
        return idxs

    def indexes_to_labels(self, indexes):
        return [self.idx_to_str[k] for k in indexes]

    
class PadChestCovid19DataHandler:
    
    def __init__(self, nb_elements_padchest=10, nb_elements_covid19=10,
                 padchest_start_idx = 0, padchest_end_idx = None,
                 covid19_start_idx = 0, covid19_end_idx = None,
                 shuffle = False, augment=False, image_size=(299,299), 
                 nchannels = 3, normalize=True,
                 tree_file = '/mnt/ssd/covid19_tree_term_CUI_counts_image_covid_posi.csv',
                 h5_file_padchest = '/mnt/ssd/padchest_pa_299.hdf5',
                 df_file_padchest =  '/mnt/ssd/padchest_pa_1024_rs.csv',
                 h5_file_covid19 = '/mnt/ssd/covid19_20200517.hdf5',
                 df_file_covid19 =  '/mnt/ssd/covid19_20200517_with_test_date_qc_with_reports.csv',
                 augmentation_coefficients=[15,15,5,10]):
        
        self.dhpadchest = PadChestDataHandler(
            nb_elements_padchest, padchest_start_idx, padchest_end_idx,
            shuffle, augment, image_size, nchannels, normalize, 
            tree_file, h5_file_padchest, df_file_padchest, augmentation_coefficients
        )

        self.dhcovid19 = PadChestDataHandler(
            nb_elements_covid19, covid19_start_idx, covid19_end_idx,
            shuffle, augment, image_size, nchannels, normalize, 
            tree_file, h5_file_covid19, df_file_covid19, augmentation_coefficients
        )
        
        self.size = self.dhpadchest.size + self.dhcovid19.size
        self.nb_elements = self.dhpadchest.nb_elements + self.dhcovid19.nb_elements
        print(self.size)
        print(int(self.size / self.nb_elements) + int(self.size % self.nb_elements > 0))
        
    def get_sample(self):
        xp, yp = self.dhpadchest.get_sample()
        xc, yc = self.dhcovid19.get_sample()
        return np.concatenate((xp,xc)), np.concatenate((yp,yc))
    
    def gen_batch(self):
        while 1:
            x, y = self.get_sample()
            yield (x, y)
            
    def steps_per_epoch(self):
        return int(self.size / self.nb_elements) + int(self.size % self.nb_elements > 0)

    