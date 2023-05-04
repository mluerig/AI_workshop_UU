# -*- coding: utf-8 -*-
"""
Created on Thu May  4 23:22:56 2023

@author: mluerig
"""

#%% load modules

import phenopype as pp
import os
import cv2

#%% killswitch for frozen windows

cv2.destroyAllWindows() 

#%% pp project


## whole body segmentation
proj = pp.Project(r"C:\Users\mluerig\Desktop\cnn_demo")
proj.add_model(r"D:\science\projects\2021_odonata_scans\models\keras\01_full_body.h5", model_id="fullbody_v1")

## run loop
for path in proj.dir_paths:
    pp.Pype(path, tag="v1")

## within body segmentation
proj = pp.Project(r"C:\Users\mluerig\Desktop\cnn_demo")
proj.add_model(r"D:\science\projects\2021_odonata_scans\models\keras\02_abdomen_v2.h5", model_id="abdomen_v2")
proj.add_model(r"D:\science\projects\2021_odonata_scans\models\keras\02_thorax_v2.h5", model_id="thorax_v2")
proj.add_model(r"D:\science\projects\2021_odonata_scans\models\keras\02_pronotum_v2.h5", model_id="pronotum_v2")
proj.add_model(r"D:\science\projects\2021_odonata_scans\models\keras\02_head_v2.h5", model_id="head_v2")

for path in proj.dir_paths:
    pp.Pype(path, tag="v2")
    
    proj.export_zip(images=True)
