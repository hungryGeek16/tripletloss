import os
import random
txt = []
count=0
dir = 'images/'  #Edit this path to your folder of images.
labels = []
for dirname in os.listdir(dir):  # List of directories present inside the specified folder which are classes
    for labs in os.listdir(dir+'/'+dirname):  # List of images containing per class
        txt.append(dirname+'/'+labs+' '+str(count)+'\n')  # Appending the path of images to a list
    count+=1
    labels.append(dirname+'\n')  # Append Labels to seperate list
random.shuffle(txt) # Randomly shuffiling the list
with open("train.txt", "a") as file1:  # Appending the list to text file.
  file1.writelines(txt[0:int(len(txt)*1)]) 
#with open("test_fin.txt", "a") as file1:
#  file1.writelines(txt[int(len(txt)*0.8):])
#with open("labels.txt", "a") as file1:
#  file1.writelines(labels)     
