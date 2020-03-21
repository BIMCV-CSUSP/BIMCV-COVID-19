#!/usr/bin/env python3
####################################################
#Imports
####################################################
import os
#os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID";

# The GPU id to use, usually either "0" or "1";
#os.environ["CUDA_VISIBLE_DEVICES"]="0";
import sys
import keras
import tensorflow as tf
import fnmatch
import random
import numpy as np
import re
import math
import pickle
import pandas as pd
from sklearn import metrics
#from utils import save_metrics
#from make_charts import make_charts
from my_data_generator import DataGenerator
from keras.applications.vgg16 import VGG16
from keras.layers import Input, AveragePooling2D, Flatten, Dense, Dropout, Dense
from keras.models import Model
from keras.optimizers import Adam

####################################################
# Variables
####################################################
is_training=True
y, x, in_channel = 724, 200, 1
batch_size = 250
epochs = 1


#config = tf.ConfigProto()
#config.gpu_options.allow_growth=True
sess = tf.Session()
output=4
dataset="pneumo"

####################################################
# Model
####################################################
input_layer = keras.layers.Input(shape=(x, x, in_channel))
baseModel = VGG16(weights=None, include_top=False,
    input_tensor=input_layer)

# construct the head of the model that will be placed on top of the
# the base model
headModel = baseModel.output
headModel = AveragePooling2D(pool_size=(4, 4))(headModel)
headModel = Flatten(name="flatten")(headModel)
headModel = Dense(64, activation="relu")(headModel)
headModel = Dropout(0.5)(headModel)
headModel = Dense(output, activation="softmax")(headModel)

# place the head FC model on top of the base model (this will become
# the actual model we will train)
model = Model(inputs=baseModel.input, outputs=headModel)
opt=Adam()
model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
model.summary()

####################################################
# Read File Data
####################################################
try: os.mkdir("./models") except: pass
try: os.mkdir("./log") except: pass
model_filename='models/cnn_classifier-2D.hdf5'
log_filename='log/cnn-classifier-2D.log'


df_pneumo_2d = pd.read_csv( sys.argv[1] , sep="\t" )
# Select only PA proyections

if is_training:
    # Train selection
    data_filter  = df_pneumo_2d['Projection']=='PA'
    data_filter &= df_pneumo_2d['Partition']=='tr'
    #data_filter = data_filter[:int(len(data_filter)/2.)]
    data_generator_train = DataGenerator( df_pneumo_2d[ data_filter ], y, x, in_channel, indexes_output=[True,True,False,False], batch_size=batch_size, data_augmentation=False, reconstruction=False, softmax=True )
    # Development selecction
    data_filter  = df_pneumo_2d['Projection']=='PA'
    data_filter &= df_pneumo_2d['Partition']=='dev'
    #data_filter = data_filter[:int(len(data_filter)/2.)]
    data_generator_dev = DataGenerator( df_pneumo_2d[ data_filter ], y, x, in_channel, indexes_output=[True,True,False,False,False], batch_size=batch_size, data_augmentation=False, reconstruction=False, softmax=True )
## Test selection (in proccess...)
#data_filter  = df_pneumo_2d['Projection']=='PA'
#data_filter &= df_pneumo_2d['Partition']=='te'
#df_pneumo_2d_test=df_pneumo_2d[ data_filter ]

#data_generator_test = DataGenerator_test( df_pneumo_2d[ data_filter ], y, x, in_channel, indexes_output=[True,True,False,False,False], batch_size=1, data_augmentation=False, reconstruction=False, softmax=True )

####################################################
# Loggers
####################################################

# the best loss and accuracy and last trained model are saved
if is_training:
    csv_logger = keras.callbacks.CSVLogger( log_filename )
    checkpoint1 = keras.callbacks.ModelCheckpoint( model_filename + '-loss', monitor='val_loss', verbose=1, save_best_only=True,  save_weights_only=False, mode='min',  period=1 )
    checkpoint2 = keras.callbacks.ModelCheckpoint( model_filename + '-last', monitor='val_loss', verbose=1, save_best_only=False, save_weights_only=False, mode='auto', period=1 )
    checkpoint3 = keras.callbacks.ModelCheckpoint( model_filename + '-acc', monitor='val_acc', verbose=1, save_best_only=False, save_weights_only=False, mode='auto', period=1 )



####################################################
# Train
####################################################

    print("Training")
    train = model.fit_generator(data_generator_train, epochs=epochs, verbose=1, validation_data=data_generator_dev, callbacks = [checkpoint1, checkpoint2, checkpoint3, csv_logger])
    model.save( model_filename )
