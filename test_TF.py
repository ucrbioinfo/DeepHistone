
# coding: utf-8

# In[28]:


from __future__ import print_function
from __future__ import division

from collections import OrderedDict
import os
import sys
import warnings

import argparse
import logging
import h5py as h5
import numpy as np
import pandas as pd
import scipy.io

import six
from six.moves import range
import csv
import math as ma
from sklearn.metrics import roc_auc_score, confusion_matrix, average_precision_score,roc_curve,auc,precision_recall_curve
from keras.preprocessing import sequence
from keras.optimizers import RMSprop,Adam, Adadelta, Nadam, Adamax, SGD, Adagrad
from keras.models import Sequential
from keras.layers.core import  Dropout, Activation, Flatten
from keras.regularizers import l1,l2,l1_l2
from keras.constraints import maxnorm
#from keras.layers.recurrent import LSTM, GRU
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.layers import Conv1D, MaxPooling1D, Dense, LSTM, Bidirectional
from sklearn.ensemble import GradientBoostingClassifier
import matplotlib.pyplot as plt

import pydot
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot
from keras.utils import plot_model


# In[29]:


#building model
model = Sequential()
model.add(Dense(units=256, input_dim= 30, activation="relu",kernel_initializer='glorot_uniform')) 
model.add(Dropout(0.3))
model.add(Dense(units=180,  activation="relu",kernel_initializer='glorot_uniform'))
model.add(Dropout(0.3))
model.add(Dense(units= 60, activation="relu",kernel_initializer='glorot_uniform')) 
model.add(Dense(units=1,  activation="sigmoid"))
model.summary()


# In[30]:


adam = Adam(lr = 0.0001)
model.compile(loss='binary_crossentropy', optimizer=adam, metrics=['accuracy'])
#model.load_weights('HistoneMark_H3K27me3_TF_ncl_H1.hdf5')
model.load_weights(sys.argv[1])


# In[31]:


#h5filename = "histonemodTF_resample_ncl.h5"
h5filename = sys.argv[2]
h5file = h5.File(h5filename,'r')
input_features = h5file['input/H3K27me3_RPKM']
output_H3K4me3 = h5file['output/H3K27me3']
input_features = np.array(input_features)
output_H3K4me3 = np.array(output_H3K4me3)
output_H3K4me3_reshape = output_H3K4me3.reshape(len(output_H3K4me3),1)


# In[32]:


#combine the label with input dna  
input_features_label = np.concatenate((input_features,output_H3K4me3_reshape), axis=1)
H3K4me3_df = pd.DataFrame(output_H3K4me3)
pos_label= H3K4me3_df.loc[H3K4me3_df.iloc[:,0]==1]
pos_label_ix = np.array(pos_label.index)
neg_label = H3K4me3_df.loc[H3K4me3_df.iloc[:,0]==0]
neg_label_ix = np.array(neg_label.index)
pos_sam_H3K4me3 = input_features_label[pos_label_ix,:]
neg_sam_H3K4me3 = input_features_label[neg_label_ix,:]
np.random.shuffle(pos_sam_H3K4me3)
np.random.shuffle(neg_sam_H3K4me3)
print(pos_sam_H3K4me3.shape)
print(neg_sam_H3K4me3.shape)


# In[33]:


train_neg_sample = int(ma.ceil(neg_sam_H3K4me3.shape[0] *0.7))
train_pos_sample = int(ma.ceil(pos_sam_H3K4me3.shape[0] *0.7))
train_neg_H3K4me3 = neg_sam_H3K4me3[0:train_neg_sample,:]
train_pos_H3K4me3 = pos_sam_H3K4me3 [0:train_pos_sample,:]
train_neg_pos_H3K4me3 = np.concatenate((train_neg_H3K4me3, train_pos_H3K4me3),axis = 0)
np.random.shuffle(train_neg_pos_H3K4me3)
X_train_H3K4me3 = train_neg_pos_H3K4me3[:,0:30]
Y_train_H3K4me3 = train_neg_pos_H3K4me3[:,30]
Y_train_H3K4me3 = np.array(Y_train_H3K4me3, dtype='int8')
frq = np.bincount(Y_train_H3K4me3)
#print(frq)
print(X_train_H3K4me3.shape)
print(Y_train_H3K4me3.shape)


# In[34]:


#validation set
val_neg_sample = train_neg_sample + int(ma.ceil(neg_sam_H3K4me3.shape[0] *0.1))
val_pos_sample = train_pos_sample + int(ma.ceil(pos_sam_H3K4me3.shape[0] *0.1))
val_neg_H3K4me3 = neg_sam_H3K4me3[train_neg_sample:val_neg_sample,:]
val_pos_H3K4me3 = pos_sam_H3K4me3[train_pos_sample:val_pos_sample,:]
val_neg_pos_H3K4me3 = np.concatenate((val_neg_H3K4me3, val_pos_H3K4me3),axis = 0)
np.random.shuffle(val_neg_pos_H3K4me3)
X_val_H3K4me3 = val_neg_pos_H3K4me3[:,0:30]
Y_val_H3K4me3 = val_neg_pos_H3K4me3[:,30]
Y_val_H3K4me3 = np.array(Y_val_H3K4me3, dtype='int8')
frq = np.bincount(Y_val_H3K4me3)
print(frq)
print(X_val_H3K4me3.shape)
print(Y_val_H3K4me3.shape)   
print(X_val_H3K4me3.shape)


# In[35]:


#test set
test_neg_H3K4me3 = neg_sam_H3K4me3[val_neg_sample:,:]
test_pos_H3K4me3 = pos_sam_H3K4me3 [val_pos_sample:,:]
test_neg_pos_H3K4me3 = np.concatenate((test_neg_H3K4me3, test_pos_H3K4me3),axis = 0)
np.random.shuffle(test_neg_pos_H3K4me3)
X_test_H3K4me3 = test_neg_pos_H3K4me3[:,0:30]
Y_test_H3K4me3 = test_neg_pos_H3K4me3[:,30]
Y_test_H3K4me3 = np.array(Y_test_H3K4me3, dtype='int8')
frq = np.bincount(Y_test_H3K4me3)
print(frq)
print(X_test_H3K4me3.shape)
print(Y_test_H3K4me3.shape)


# In[36]:


y_pred = model.predict(X_test_H3K4me3)
aupr = average_precision_score(Y_test_H3K4me3, y_pred)
print(aupr)
print(roc_auc_score(Y_test_H3K4me3, y_pred))

#python test_H3K27me3_TF.py HistoneMark_H3K27me3_TF_ncl_H1.hdf5 histonemodTF_resample_ncl.h5
#python test_TF.py weights/TFbinding/HistoneMark_H3K27me3_TF_ncl_H1.hdf5 histonemodTF_resample_ncl.h5

