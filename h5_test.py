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
from sklearn.decomposition import PCA
file = '/glb/am/sepco/seis/epw_ua_seisproc_scratch_0014/jpdata/epw_imaging/tomo_dnn_19/qc_data/cgg/cgg_post-59000-46036-1.hdf5'
f= h5.File(file,"r")
trc = f['Traces']['TraceData']
seis = np.array(trc)
s_scale = (seis-seis.flatten().mean())/seis.flatten().std()
#plt.imshow(s_scale.T,vmax=.1*np.max(s_scale),vmin=-.1*np.max(s_scale),cmap='seismic',aspect=.03)
#plt.imshow(seis.T,vmax=.1*np.max(seis),vmin=-.1*np.max(seis),cmap='seismic',aspect=.03)
#plt.title(i[:-5])
#    plt.savefig(i[:-5]+'.png', bbox_inches='tight')
#plt.

#plt.show()
scalar = 0.25
pca = PCA(n_components=2)
pca2 = PCA(n_components=20)
pca.fit(s_scale)
pca2.fit(s_scale)
print(pca.explained_variance_ratio_);
print(sum(pca.explained_variance_ratio_))
print(pca2.explained_variance_ratio_);
print(sum(pca2.explained_variance_ratio_))
ps_scale = pca.inverse_transform(pca.transform(s_scale))
ps2_scale = pca2.inverse_transform(pca2.transform(s_scale))
plt.imshow(ps_scale.T,vmax=1,vmin=-1,cmap='seismic',aspect=.075)
plt.show()
plt.imshow(ps2_scale.T,vmax=1,vmin=-1,cmap='seismic',aspect=.075)
plt.show()
plt.imshow(ps_scale.T-s_scale.T,vmax=1,vmin=-1,cmap='seismic',aspect=.075)
plt.show()
plt.imshow(ps2_scale.T-s_scale.T,vmax=1,vmin=-1,cmap='seismic',aspect=.075)
plt.show()
plt.hist((ps_scale-s_scale).flatten(), bins=300,color='blue',normed=True);
plt.hist((ps2_scale-s_scale).flatten(),bins=300,color='red', alpha=0.5,normed=True,range=[-2,2]);
plt.show()
