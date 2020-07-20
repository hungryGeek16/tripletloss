import os
import codecs

print(7)

class sampledata():

    global _sample_person
    global _sample_negative
    global _sample
    global _sample_label
    

    def __init__(self):
        self._sample_person = {}
        self._sample_negative = {}
        self._sample = []
        self._sample_label = {}
        lines = open('/home/rahul/trip/data/train.txt','r')
        for line in lines:
            print(line)
            personname = line.split('/')[0]
            picname = line.split(' ')[0]
            self._sample.append(picname)
            if personname in self._sample_person.keys():
                self._sample_person[personname].append(picname)
            else:
                self._sample_person[personname] = []
                self._sample_person[personname].append(picname)
            self._sample_label[personname] = int(line.split(' ')[1])

if __name__ == '__main__':

    sample = sampledata()
