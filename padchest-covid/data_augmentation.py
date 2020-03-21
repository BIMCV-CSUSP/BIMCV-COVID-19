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

# image_path="adni_opt_3d_freemask_rgb/116_S_4338/MPRAGE/2012-02-02_14_08_03.0/S139612/sub-1164338_ses-1_T1w.npy"
# numpy_matrix=numpy.load(image_path, allow_pickle=True)
#
# numpy_image = numpy_matrix[0][:,:,:,0]
# numpy_image.dtype
# numpy_mask = numpy_matrix[0][:,:,:,1:]
#
# plt.imshow(numpy_image[128,:,:],cmap="gray")
# plt.imshow(numpy_mask[128,:,:])
# factor  = float(numpy.around(numpy.random.uniform(0.8, 1.2, size=1), 2))
# factor
# numpy_image.max()
# numpy_image[100,100,100]/255
# numpy_image = intensifyit(numpy_image, factor)
# numpy_image = numpy.minimum( 255, numpy_image )
# numpy_image = numpy.maximum( 0, numpy_image )
# numpy_image[100,100,100] /255
# plt.imshow(numpy_image[:,128,:],cmap="gray")
# theta1 = float(numpy.around(numpy.random.uniform(-50.0,50.0, size=1), 3))
# theta2 = float(numpy.around(numpy.random.uniform(-50.0,50.0, size=1), 3))
# theta3 = float(numpy.around(numpy.random.uniform(-50.0,50.0, size=1), 3))
# theta1
# theta2
# theta3
# numpy_matrix[0].shape
# thisim  = rotateit(numpy_image, theta1,theta2,theta3)
# plt.imshow(thisim[:,128,:],cmap="gray")
# offset  = list(numpy.random.randint(-10,10, size=3))
# offset
# numpy_image_t = translateit_fast(numpy_matrix[0], offset)
# plt.imshow(numpy_image_t[:,128,:,0],cmap="gray")
#
#
#
# scalefactor  = float(numpy.around(numpy.random.uniform(0.9, 1.05, size=1), 2))
# scalefactor
# plt.imshow(thisim[:,128,:],cmap="gray")
