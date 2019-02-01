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

To run run the test_tf.py file

```
$ python test_tf.py weights/TFbinding/*.hdf5 <directory of RPKM file> <output file>

```
where * can be any one of the files located in the directory of weights/TFbinding. A sample <RPKM> file is shown
in the example.  <output file> refers to the directory of the output file where predicted histone ptm will be stored
