#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:03:12 2018

@author: yuanneu
"""

import numpy as np
import scipy as sc
import scipy.io as sio  
import math
import random
import cmath
import re
import pickle 
import time
import sys


Name='FinalN'
TimeList=[0,4,6,8,9,11]
SizeList=[200,200,200,200,5,8]
At=[[],[],[],[],[],[]]
TL=[]
TS=[]
for timefa in range(124):
    cst=Name+str(1)+'AUC'+str(timefa)+'.p'
    try:
        with open(cst, 'rb') as f:
            d = pickle.load(f)                  
        for Method in range(6):
            nam=TimeList[Method]
            Size=SizeList[Method]
            print (nam,Size)
            At[Method].append(d['Time'][nam][range(Size)])
    except:        
        print ('error',timefa)
        pass
    
for i in range(6):
    TL.append(np.mean(np.array(At[i]),0))
    TS.append(np.std(np.array(At[i]),0))
    
Cp={}
Cp['time']=TL
Cp['tstd']=TS
csts='FinalNtime.p'
pickle.dump(Cp,open(csts,"wb")) 
