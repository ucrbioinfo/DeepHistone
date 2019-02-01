
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

	

#building model
model = Sequential()
model.add(Dense(units=512, input_dim=2080, activation="relu", kernel_initializer='glorot_uniform'))
model.add(Dropout(0.5))
model.add(Dense(units=180, activation="relu",kernel_initializer='glorot_uniform'))
model.add(Dropout(0.5))
model.add(Dense(units=70, activation="relu",kernel_initializer='glorot_uniform'))
model.add(Dense(units=1, activation="sigmoid"))


adam = Adam(lr = 0.0001)
model.compile(loss='binary_crossentropy', optimizer=adam, metrics=['accuracy'])

#loding the weight file
model.load_weights(sys.argv[1])


# loading the kmer file
testfile = np.loadtxt(sys.argv[2], delimiter= ',', skiprows=1)
y_pred = model.predict(testfile)


y_pred = y_pred>0.5
np.savetxt(sys.argv[3], y_pred, delimiter=",")


#python test_seq.py weights/Seq/HistoneMark_H3K4me3_Seq_ncl_H1.hdf5 SampleData/kmer_count.csv output.txt 
