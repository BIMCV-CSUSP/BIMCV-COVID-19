import scipy
import os
import numpy
import matplotlib.pyplot as plt
from scipy.ndimage.interpolation import zoom
from scipy.ndimage.interpolation import rotate

from matplotlib import cm

def translateit_fast_2d(image, offset, fill_value=0):
    """
       the funtion translate the content of a one image 
       with the offset paremetre
    """
    newimg  = numpy.zeros_like(image)
    if offset[0] > 0:
        newimg[offset[0]:,:,:] = image[:-offset[0],:,:]
    elif offset[0] < 0:
        newimg[:offset[0],:,:] = image[-offset[0]:,:,:]
    else:
        newimg=image

    if offset[1] > 0:
        newimg[:,offset[1]:,:] = newimg[:,:-offset[1],:]
    elif offset[1] < 0:
        newimg[:,:offset[1],:] = newimg[:,-offset[1]:,:]
    else:
        pass
    return newimg

def scaleit_2d(image, factor, isseg=False):
    """
        the funtion scale the content of a one image 
        with the factor paremetre
    """
    order = 0 if isseg == True else 3
    #print(image.shape)
    height, width = image.shape
    zheight       = int(numpy.round(factor * height))
    zwidth        = int(numpy.round(factor * width))
    #zdepth              = int(numpy.round(factor * depth))

    if factor < 1.0:
        newimg  = numpy.zeros_like(image)
        #print(newimg.shape)
        row     = (height - zheight) // 2
        col     = (width - zwidth) // 2
        #layer   = (depth - zdepth) // 2
        newimg[row:row+zheight, col:col+zwidth] = zoom(image, (float(factor), float(factor)), order=order, mode='nearest')[0:zheight, 0:zwidth]

        return newimg

    elif factor > 1.0:
        row     = (zheight - height) // 2
        col     = (zwidth - width) // 2
        #layer   = (zdepth - depth) // 2

        newimg = zoom(image[row:row+zheight, col:col+zwidth], (float(factor), float(factor)), order=order, mode='nearest')

        extrah = (newimg.shape[0] - height) // 2
        extraw = (newimg.shape[1] - width) // 2
        #extrad = (newimg.shape[2] - depth) // 2
        newimg = newimg[extrah:extrah+height, extraw:extraw+width]

        return newimg

    else:
        return image

def resampleit(image, dims, isseg=False):
    """
        the funtion resample one image 
        with the dims paremetre
    """
    order = 0 if isseg == True else 5

    image = zoom(image, numpy.array(dims)/numpy.array(image.shape, dtype=numpy.float32), order=order, mode='nearest')

    if image.shape[-1] == 3: #rgb image
        return image
    else:
        return image if isseg else (image-image.min())/(image.max()-image.min())

def rotateit_2d(image, theta1, isseg=False):
    order = 0 if isseg == True else 5
    newimage=image
    if theta1 != 0.0:
        newimage = rotate(newimage, float(theta1), reshape=False, order=order)
    return newimage

def intensifyit_2d(image, factor):
    """
        the funtion change the intensity of one image 
        with the dims paremetre
    """
    
    return image*float(factor)

