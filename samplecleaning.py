import os
import sys
import warnings
from sklearn.manifold import TSNE
from sklearn.decomposition import TruncatedSVD
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from imblearn.under_sampling import OneSidedSelection, NeighbourhoodCleaningRule
import h5py as h5

if __name__ == '__main__':


 skiprows = 1 
 input_RPKM = np.loadtxt(sys.argv[1], delimiter=',', skiprows=skiprows)
 input_features = input_RPKM
 X = input_features

 out_label = np.loadtxt(sys.argv[2], skiprows=skiprows)
 y = np.array(out_label, dtype='int8')  
 frq  = np.bincount(y)    



# Apply NeighbourhoodCleaningRule
 ncl = NeighbourhoodCleaningRule(random_state = 42, return_indices=True)
 X_resampled, y_resampled, idx_resampled = ncl.fit_sample(X, y)
 np.savetxt('features.txt', X_resampled, delimiter=",")
 np.savetxt('labels.txt', y_resampled, delimiter=",")

# python samplecleaning.py SampleData/TF_CM.csv SampleData/TSS_Label.txt 
