#!/usr/bin/env python3
# coding: utf-8
import pathlib

import SimpleITK as sitk
import os
import numpy as np
import sys

download_path = sys.argv[1]
output_path = sys.argv[2]

for p in pathlib.Path(download_path).glob("*.dcm"):
    path_to_dicom = str(p)
    # Reads the images and saves them as png
    path_to_png = os.path.join(output_path, p.parts[-1].replace( ".dcm",".png"))

    sitk_img = sitk.ReadImage(path_to_dicom)
    img = sitk.GetArrayFromImage(sitk_img)[0, :, :]
    sitk.WriteImage(sitk_img, path_to_png)

    # Re-reads the image for sanity check
    img_dcm = sitk.GetArrayFromImage(sitk.ReadImage(path_to_dicom))[0, :, :]
    img_png = sitk.GetArrayFromImage(sitk.ReadImage(path_to_png))

    if np.sum(np.abs(img_dcm - img_png)) > 100:
        print(p)

