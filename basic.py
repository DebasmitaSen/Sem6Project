import cv2
import numpy as np
import face_recognition
import dlib

imgpagu = face_recognition.load_image_file('ImagesBasic/chiku.webp')
imgpagu= cv2.cvtColor(imgpagu,cv2.COLOR_BGR2RGB)
imgtest = face_recognition.load_image_file('ImagesBasic/virat.jpg')
imgtest= cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)

cv2.imshow('garden',imgpagu)
cv2.imshow('fan',imgtest)
cv2.waitkey(0)