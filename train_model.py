# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 11:04:08 2023

@author: KORINGA UMANG
"""

from imutils import paths
import face_recognition
import pickle
import cv2
import os
# import matplotlib.pyplot as plt
# import numpy as np


path = "F:\collage\sem-6\Project\WebSite\static\\assets\studentsImg"
imagePath = []
for root, dirs, files in os.walk(path):
    imagePath.extend(dirs)
print(len(imagePath))

known_Encodings = []
known_Names = []
print(imagePath)
for (i, ip) in enumerate(imagePath):
    name = ip.split(os.path.sep)[0]
    ls = os.listdir(path+'/'+name)
    for images in ls:
        #print(name)
        #print(path+'/'+name+'/'+images)
        img = cv2.imread(path+'/'+name+'/'+images,0)
        #print(img)
        #img = cv2.resize(img,(200,200))
        #cv2.imshow("image",img)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb,model = 'hog')
        encodings = face_recognition.face_encodings(rgb, boxes)
        for encoding in encodings:
            known_Encodings.append(encoding)
            known_Names.append(name)
        if True:
            break
    print(name)

data  = {"encodings": known_Encodings, "names": known_Names }
f = open("F:\collage\sem-6\Project\\Website\\face_enc2","wb")
f.write(pickle.dumps(data))#to open file in write mode
f.close()#to close file
cv2.waitKey()
cv2.destroyAllWindows()