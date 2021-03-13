import cv2 as cv
import os
import numpy as np
traindata = []
imgs = "/home/carl/nodelearn/imgs"
list = os.listdir(imgs)
list.sort()
len = len(list)
print(len)
for img in list: 
         test = np.array(cv.resize(cv.imread(imgs + "/" + img , cv.IMREAD_GRAYSCALE) , (1 , 1)))
         if (test == 255):
             list.remove(img)
for img in list:
    arrey = cv.resize(cv.imread(imgs + "/" + img , cv.IMREAD_GRAYSCALE) , (50 , 50))
    if img[0] == "a":
     traindata.append([arrey, [1, 0]])
    else:
     traindata.append([arrey, [0, 1]])
np.save("traindata.npy" , traindata)

