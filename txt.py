import os
import random
txt = []
count=0
dir = 'images/'  #Edit this path to your folder of images.
labels = []
for dirname in os.listdir(dir):
    for labs in os.listdir(dir+'/'+dirname):
        txt.append(dirname+'/'+labs+' '+str(count)+'\n')
    count+=1
    labels.append(dirname+'\n')  
random.shuffle(txt)
with open("train.txt", "a") as file1:
  file1.writelines(txt[0:int(len(txt)*1)])
#with open("test_fin.txt", "a") as file1:
#  file1.writelines(txt[int(len(txt)*0.8):])
#with open("labels.txt", "a") as file1:
#  file1.writelines(labels)     
