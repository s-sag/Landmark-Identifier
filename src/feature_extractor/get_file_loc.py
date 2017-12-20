import numpy as np
import os

def binarize(i, max):
    foo = [0]*max
    foo[i] = 1
    return foo

first_loc = os.getcwd()
im_src = "../../../data/2/images"
os.chdir(im_src)
file_names = "input.txt"
label_names = "labels.txt"
file_of_label_of_files = "labels.npy"

labels_names = []
files = []
labels = []

for num, loc in enumerate(sorted(os.listdir(os.getcwd()))):
    labels_names.append("{}\t{}".format(num, loc))
    for im in os.listdir(os.getcwd()+"/"+loc):
        labels.append(binarize(num, len(os.listdir(os.getcwd()))))
        #files.append(os.getcwd()+"/"+ loc +"/"+im)

os.chdir(first_loc)
'''file1 = open(file_names, "w")
for file in files:
    file1.write("{}\n".format(file))

file_labels = open(label_names, "w")
for label in labels_names:
    file_labels.write("{}\n".format(label))'''

labels = np.asarray(labels)
np.save(file_of_label_of_files, labels)