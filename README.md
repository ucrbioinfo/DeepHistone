# DeepHistone
DeepHistone is a deep learning architecture for predicting histone PTMs from transcription factor
binding data and the primary DNA sequence. For dataset, we considered three-four histone PTMs that are
known to be relevant for transcription, namely H3K4me3, H3K9ac,
H3K27ac for H1 ES cell lines, K562 erythroleukemia cell lines, and GM12878
lymphoblastoid  cell lines. For cell line H1, we also considered
H3K27me3.

<h3>Dependency </h3>

1. Python==2.7
2. keras==2.1.3
3. scikit-learn==0.19.1
4. numpy==1.13.3
5. h5py==2.7.0
6. pandas==0.20.3
7. tensorflow-gpu==1.5.0

<h4>Run code</h4>

**1.samplecleaning.py:** This script is used for data cleaning for both Sequence and TF bindings. To run it:
  
```
$ python samplecleaning.py <features file> <label file> 

```

**Parameters:**

**features file** contains the features of the sample e.g, 6mer count, normalized readcount 

**label file** contains the binary label of the sample

**Return:**

**features.txt:** contains reduced samples with feature vectors    

**labels.txt:** contains the labels of the reduced samples

For Example:
```
$ python samplecleaning.py SampleData/TF_CM.csv SampleData/TSS_Label.txt 

```


**2. test_tf.py:** This script is used to get the Histome PTM prediction accuracy from TF bindings. To run it: 

```
$ python test_tf.py <Cell line> <Weight File for Histone PTM for the Cell line > <Normalized Read count file> <output file>

```
**Parameters:**

**Cell line** can be any one of the three: H1, K562 and GM12878. 

**Weight File for Histone PTM for the Cell line** can be any one of the files located in the directory of weights/TFbinding.

**Normalized Read count file** is the normalized readcount file of TFs for Specific histone PTM for a specific cell line. A sample of it is shown in the 'SampleData' Directory.

**output file** refers to the directory of the output file where predicted histone ptm will be stored


**Return:** 

Predicted histone ptm of DeepHistone in **output file**
  
For Example:
```
$python test_TF.py GM12878 weights/TFbinding/HistoneMark_H3K9ac_TF_ncl_GM12878.hdf5  SampleData/TF_GM12878.txt output.txt
```

**3. test_Com_TF.py:** This script is used to get the Histome PTM prediction accuracy from TF binding using 17 common TFs across three cell lines: H1, K562 and GM12878  

```
$ python test_Com_tf.py  <Weight File for Histone PTM for the Cell line > <Normalized Read count file> <output file>

```
**Parameters:**

**Weight File for Histone PTM for the Cell line** can be any one of the files located in the directory of weights/TFbinding.

**Normalized Read count file** is the normalized readcount file of TFs for Specific histone PTM for a specific cell line. A sample of it is shown in the 'SampleData' Directory.

**output file** refers to the directory of the output file where predicted histone ptm will be stored


**Return:** 

Predicted histone ptm of DeepHistone in **output file**

For Example :

```
python test_Com_TF.py weights/CrossCells/HistoneMark_H3K4me3_K562_GM.hdf5 SampleData/Common_TF_GM12878.txt output.txt 

```

**4. test_Seq.py:** This script is used to get the Histome PTM prediction accuracy from Sequence centered around the TSS. 
Features are vector of length 2080 of 6-mer count.
  

```
$ python test_Seq.py <Weight File for Histone PTM for the Cell line > <6-mer count file> <output file>

```  

**Parameters:**

**Weight File for Histone PTM for the Cell line** can be any one of the files located in the directory of weights/Seq. 

**6-mer count file**  each row contains a vector of length 2080 6mer count. A sample  file is shown in the 'SampleData' Directory.  

**output file** refers to the directory of the output file where predicted histone ptm will be stored.


**Return:**

Predicted histone ptm of DeepHistone in **output file**
  
For example: 

```
$python test_seq.py weights/Seq/HistoneMark_H3K4me3_Seq_ncl_H1.hdf5 SampleData/kmer_count.csv output.txt 

```  
  

