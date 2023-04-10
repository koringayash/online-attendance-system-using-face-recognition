# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 17:30:13 2023

@author: KORINGA UMANG
"""

#This is for face recofnition

from imutils import paths
import face_recognition
import pickle
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

video_capture = cv2.VideoCapture(0)
   #Here parameter 0 is a path of any video use for webcam
print("check===",video_capture.isOpened())

#it is 4 byte code which is use to specify the video codec
#Various codec -- 
#DIVX, XVID, MJPG, X264, WMV1, WMV2
#fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
#output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0)

cfp = "F:\collage\sem-6\Project\dataSet\cascades\haarcascade_frontalface_alt2.xml"
fc = cv2.CascadeClassifier(cfp)

# load the harcaasc
# x = set()



student_present = set()

while True:
    data = pickle.loads(open('F:\collage\sem-6\Project\\Website\\face_enc2',"rb").read())
    known_face_encodings = data["encodings"]
    known_face_names = data["names"]
    print("Hello")
    ret, frame = video_capture.read()

    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    name = "Unknown"

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        print(name)
        student_present.add(name)
        with open('F:\collage\sem-6\Project\\Website\\present_student.txt','w') as f:
            f.write(str(student_present))
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    
        
    cv2.imshow('Video', frame)
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break



# Release everything if job is finished
cv2.destroyAllWindows()

"""
while(cap.isOpened()):
    print("H")
    ret, frame = cap.read()   #here read the frame
    
    if ret==True:
        
        gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = fc.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=6,minSize=(60,60),flags=cv2.CASCADE_SCALE_IMAGE)
        encodings = face_recognition.face_encodings(frame)
        if len(encodings)==0:
            continue
        encoding = encodings[0]
        result = face_recognition.compare_faces(data["encodings"],encoding)
        print(result)
        
        for i in range(len(result)):
            if result[i]:
                name = (data["names"][i])
                (top,right,bottom,left) = face_recognition.face_locations(frame)[0]
                cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
                cv2.putText(frame,name,(left+2,bottom+20),cv2.FONT_HERSHEY_PLAIN,0.8,(255,255,255),1)
                
        #cv2.imshow("Gray Frame",gray)
        cv2.imshow('Colorframe',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #press to exit
            break
    else:
        break
 
# Release everything if job is finished
cv2.destroyAllWindows()
"""