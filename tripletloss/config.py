import os
from numpy import *

print(3)

# Training image data path
IMAGEPATH = '/home/rahul/trip/images/'

# Snapshot iteration 
SNAPSHOT_ITERS = 10000

# Max training iteration
MAX_ITERS = 400000  # Number of epochs * number of labels

# The number of samples in each minibatch
BATCH_SIZE = 6  # number of images in each sample

