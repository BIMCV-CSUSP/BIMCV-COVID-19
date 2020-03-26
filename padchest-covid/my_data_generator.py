####################################################
#Imports
####################################################

import numpy as np
import os
import keras
from keras.preprocessing.image import img_to_array
from skimage.transform import resize
from PIL import Image
from data_augmentation import translateit_fast_2d as translateit_fast
from data_augmentation import scaleit_2d as scaleit
from data_augmentation import rotateit_2d as rotateit
from data_augmentation import intensifyit_2d as intensifyit

####################################################
#variables
####################################################

dict_classes={
    "C":np.array([1, 0, 0, 0]),
    "N":np.array([0, 1, 0, 0]),
    "I":np.array([0, 0, 1, 0]),
    "NI":np.array([0 , 0, 0, 1])
}

####################################################
#classes
####################################################

class DataGenerator(keras.utils.Sequence):

    ''' Initialization of the generator '''
    def __init__(self, data_frame, y, x, target_channels, indexes_output=None, batch_size=128, path_to_img="./img", shuffle=True, data_augmentation=False, reconstruction=False, softmax=False):
        # Initialization
        # Tsv data table
        self.df = data_frame
        # Image Y size
        self.y = y
        # Image X size
        self.x = x
        # Channel size
        self.target_channels = target_channels
        # batch size
        self.batch_size = batch_size
        # Boolean that allows shuffling the data at the end of each epoch
        self.shuffle = shuffle
        # Boolean that allows data augmentation to be applied
        self.data_augmentation = data_augmentation
        # Array de posiciones creada a partir de los elementos de la tabla
        self.indexes = np.arange(len(data_frame.index))
        # Array of positions created from the elements of the table
        self.path_to_img = path_to_img

    def __len__(self):
        ''' Returns the number of batches per epoch '''
        return int(np.ceil(len(self.indexes) / self.batch_size))

    def __getitem__(self, index):
        ''' Returns a batch of data (the batches are indexed) '''
        # Take the id's of the batch number "index"
        indexes = self.indexes[index*self.batch_size:(index+1)*self.batch_size]

        # Batch initialization
        X, Y = [], []

        # For each index,the sample and the label is taken. Then the batch is appended
        for idx in indexes:
            # Image and idx index tag is get
            x, y = self.get_sample(idx)
            # This image to the batch is added
            X.append(x)
            Y.append(y)
	# The created batch is returned
        return np.array(X), np.array(Y) #X:(batch_size, y, x), y:(batch_size, n_labels_types)

    def on_epoch_end(self):
        ''' Triggered at the end of each epoch '''
        if self.shuffle == True:
            np.random.shuffle(self.indexes) # Shuffles the data

    # Roberto Paredes contribution @RParedesPalacios

def get_sample(self, idx):
    '''Returns the sample and the label with the id passed as a parameter'''
    # Get the row from the dataframe corresponding to the index "idx"                                                                       
    df_row = self.df.iloc[idx]
    image = Image.open(os.path.join(self.path_to_img,df_row["ImageID"]))
    da =  np.asarray(image).shape
    #image.thumbnail((self.x,self.x), Image.ANTIALIAS)                                                                                      
    image = image.resize((self.x,self.x))
    image = np.asarray(image)
    label = dict_classes[df_row["group"]]
    image_resampled = np.reshape(image,image.shape + (self.target_channels,))
    img2=np.array(image_resampled)

    img2.setflags(write=1)

    # Data aumentation **always** if True                                                                                                   
    if self.data_augmentation:
        do_rotation = True
        do_shift = True
        do_zoom = True
        do_intense= True

        theta1 = float(np.around(np.random.uniform(-10.0,10.0, size=1), 3))
        offset = list(np.random.randint(-20,20, size=2))
        zoom  = float(np.around(np.random.uniform(0.9, 1.05, size=1), 2))
        factor = float(np.around(np.random.uniform(0.8, 1.2, size=1), 2))

        if do_rotation:
            rotateit(img2, theta1)
        if do_shift:
           translateit_fast(img2, offset)


        if do_zoom:
            for channel in range(self.target_channels):
                img2[:,...,channel] = scaleit(img2[:,...,channel], zoom)
        if do_intense:
            img2[:,...,0]=intensifyit(img2[:,...,0], factor)

    #### DA ends                                                                                                                            

    img2 = self.norm(img2)
    # Return the resized image and the label                                                                                                
    return img2, label

    def norm(self, image):
        image = image / 255.0
        return image.astype( np.float32 )
