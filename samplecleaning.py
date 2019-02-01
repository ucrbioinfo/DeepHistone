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
 #For H1 cell line set columns 30, for K562 cell line set columns 43 and for GM12878 cell line set column 51 
 usecols = [0, 1, 2, 3, 4, 5,6, 7, 8,9, 10 , 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
 skiprows=1 
 dtype = {usecols[0]: np.str, usecols[1]: np.float64, usecols[2]: np.float64, usecols[3]: np.float64, usecols[4]: np.float64, usecols[5]: np.float64, usecols[6]: np.float64,usecols[7]: np.float64, usecols[8]: np.float64,
			usecols[9]: np.float64, usecols[10]: np.float64, usecols[11]: np.float64, usecols[12]: np.float64, usecols[13]: np.float64, usecols[14]: np.float64, usecols[15]: np.float64,usecols[16]: np.float64,usecols[17]: np.float64, 
			usecols[18]: np.float64, usecols[19]: np.float64, usecols[20]:  np.float64, usecols[21]: np.float64, usecols[22]: np.float64, usecols[23]: np.float64, usecols[24]: np.float64, usecols[25]: np.float64, usecols[26]: np.float64,
			usecols[27]: np.float64, usecols[28]: np.float64, usecols[29]: np.float64, usecols[30]: np.float64}
 input_RPKM = pd.read_csv(sys.argv[1], sep=',', header=None, usecols=usecols, dtype=dtype, skiprows=skiprows)
 X = input_RPKM.values
 out_label = pd.read_table(sys.argv[2], header=None, usecols=usecols, dtype=dtype, skiprows=skiprows)
 y = int(out_label.values[:,0])
 
 # Apply NeighbourhoodCleaningRule
 ncl = NeighbourhoodCleaningRule(random_state = 42, return_indices=True)
 X_resampled, y_resampled = ncl.fit_sample(X, y)
 
 np.savetxt('features.txt', X_resampled, delimiter=",")
 np.savetxt('labels.txt', y_resampled, delimiter=",")
