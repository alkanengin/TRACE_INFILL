#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:10:40 2019

@author: uscsu2
"""

import numpy as np
import matplotlib.pyplot as plt
import h5py as h5
import os
dir = '/glb/am/sepco/seis/epw_ua_seisproc_scratch_0014/jpdata/epw_imaging/tomo_dnn_19/qc_data/gdm/'
for i in os.listdir(dir):
    print(dir+i)
    f = h5.File(dir+i,"r")
    trc = f['Traces']['TraceData']
    seis = np.array(trc)
    plt.imshow(seis.T,vmax=.1*np.max(seis),vmin=-.1*np.max(seis),cmap='seismic',aspect=.03)
    plt.title(i[:-5])
    plt.savefig(i[:-5]+'.png', bbox_inches='tight')
