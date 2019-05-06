# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:41:45 2019

@author: Carl
"""

from glob import glob
import os

Arff_Path = 'D://MSP-PODCAST//arff'
Bat_Path = 'D://MSP-PODCAST//bat'
Path ='D://MSP-PODCAST//*'
sfile = r'D://MSP-PODCAST//bat//Poadcast.bat'

if not os.path.exists(Arff_Path):
    os.makedirs(Arff_Path)        

#bat save path
if not os.path.exists(Bat_Path):
    os.makedirs(Bat_Path)   

# wav path



Files = glob(Path)
for files_path in Files:
        
    Split = files_path.split("\\")
    Input = files_path
    Output = Arff_Path + "//" +Split[-1]
    Output = Output.replace(".wav",".arff")
    Write = "SMILExtract_Release -C D://opensmile-2.3.0//config//IS10_paraling.conf -I "+ Input + " -O " + Output
    
    with open(sfile,'a') as s:
        s.write( Write + "\n" )
                