# How to Use it:

**Disclaimer:** Before diving please make sure that your concepts on Triplet Loss and FaceNet are clear. Otherwise for a short review please go through the below links.

* [FaceNet: A Unified Embedding for Face Recognition and Clustering](https://medium.com/@ahmdtaha/facenet-a-unified-embedding-for-face-recognition-and-clustering-7d34abde9)

* [Triplet Loss and Online Triplet Mining](https://omoindrot.github.io/triplet-loss)  

This is an implementation of triplet loss function is in python layer which is a support provided by caffe. Semi-hard examples are used to train the network. Refer this [link](https://github.com/luhaofang/tripletloss#setup) to compile caffe with python layer support.

**Requirements**:

* Python 3.6

* OpenCV version >= 3.4.3

* Numpy

* Pyyaml

* Codecs

* Protobuf >= 3.11.4

## Steps to run the program:

* Use txt.py to create list of images for training and place output file in data folder.
```cpp
python3 txt.py
```
* Create a folder called models and place the caffemodel in that folder.

* Change paths accordingly to the model in tripletloss/config.py.

* Change size of the input images by which the caffemodel was trained(in my case caffemodel was trained by 160 X 160) in tripletloss/blob.py and tripletloss/datalayer.py .

* Change paths accordingly in tripletloss/train.py .

* Run the below command.

```cpp
python3 train.py
```

**Note: Before running train.py, please make sure that you have set every path in every python file in tripletloss folder correctly.**

## Credits : David Lu  

**Github Profile:** [Link](https://github.com/luhaofang/tripletloss)


