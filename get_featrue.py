# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:44:47 2019

@author: Carl
"""

from glob import glob
import os
import numpy as np
import joblib
from tqdm import tqdm
import pandas as pd
#%%IS10 IS13 Compare16
def get_Feature(feat_path):
    with open(feat_path) as f:
        content_tmp = f.readlines()
        
    content = content_tmp[-1]
    content_1 = content.split(",")
    content_2 = np.array(content_1[1:-1],dtype=float).reshape(1,-1)
    return content_2
    
    
#%% mk dict
dict={}

with open('D:/MSP-PODCAST/bat/label.txt') as f:
    label_load = f.readlines()

for idx in label_load:
    if idx.startswith('MSP'):
        sub={}
        Name , sub['Emo'] , sub['Act'] , sub['Val'] , sub['Dom'] = idx.split(';')[:-1]
        Name = Name[:-4]             
        dict[Name] = sub
     
for wav_path in tqdm(glob('D:/MSP-PODCAST/arff/*')):
    Name = wav_path.split('\\')[-1][:-5]
    dict[Name]['Feature'] = get_Feature(wav_path) 

joblib.dump('D:/MSP-PODCAST/bat/MSP_Poadcast.pkl')