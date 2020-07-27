# Logs 27th July 2020:

## Utlimate Goal: Implement Triplet Loss Layer in Cpp in caffe.

* So I started out to look for data handling layer in caffe,  so I checked from previous training logs and found out that caffe calls net.cpp the most while training.

* Therefore I opened up net.cpp and saw constructor fucntions in it. Here my old habit of getting confused while lookin at the code came once again.

* The main root of this problem was that my brain is unable to digest some alien concepts such as vector inside a vector which is again template pointer to the values.

* Here I am clear with generic concepts used in cpp , but my knowledge on hybrid concepts is limited and I think I need more practice for that.

* So firstly I went look out for the concept of vector inside a vector, here I found out that vector inside a vector is a way to create 2D vectors which I somehow missed out at initial stage of understanding crtical concepts in cpp for caffe.

* Then I slowly got realized that initally my way of perspective to look into the vectors was different and now I have change that perspective to get more clear understanding on vectors in cpp

* Even same problem was faced with templates, hence same solution was applied to it.

* If look every concept individually I'll run into same situation , so i have decided to look into the exact flow from start to end in caffe and them come to conclusion.

