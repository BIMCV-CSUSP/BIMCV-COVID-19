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

        # Data aumentation
        do_rotation = True if np.random.rand() > 0.3 else False
        do_shift = True if np.random.rand() > 0.3 else False
        do_zoom = True if np.random.rand() > 0.3 else False
        do_intense= True if np.random.rand() > 0.3 else False
        theta1 = 0
        offset = [0, 0]
        zoom  = 1.0
        factor = 1.0
        if self.data_augmentation and np.random.rand() > 0.3: # Perform data augmentation

            theta1 = float(np.around(np.random.uniform(-20.0,20.0, size=1), 3))
            offset = list(np.random.randint(-15,15, size=2))
            zoom  = float(np.around(np.random.uniform(0.9, 1.05, size=1), 2))
            factor = float(np.around(np.random.uniform(0.8, 1.2, size=1), 2))
            if do_rotation:
                rotateit(image_resampled, theta1)
            if do_shift:
                translateit_fast(image_resampled, offset)
            if do_zoom:
                for channel in range(self.target_channels):
                    image_resampled[:,...,channel] = scaleit(image_resampled[:,...,channel], zoom)
            if do_intense:
                image_resampled[:,...,0]=intensifyit(image_resampled[:,...,0], factor)

        image_resampled = self.norm(image_resampled)
        # Return the resized image and the label
        return image_resampled, label

    def norm(self, image):
        image = image / 255.0
        return image.astype( np.float32 )
