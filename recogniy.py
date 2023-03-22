import cv2
import dlib
import face_recognition
import numpy as np
import connection
import attendence
import os

#code to connect to database and collect images and the id of student
#array name must be 'images'
#array for id must be 'classID'


def findEncodings(image):
    encodeList = []
    for img in image:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)[0]
        encodeList.append(encoded_face)
    return encodeList
#image=cv2.imread("G:/Debasmita files/project/sample.jpg")
list1=connection.images
k="C:/Users/mouli/Documents/GitHub/Sem6Project/"
var="/img"
count=1
list2=[]
list3=[]
for i in  range (1,6):
    cn="%s"%i
    var2=var+cn+".jpg"
    i=i+1
    list2.append(var2)
for i in range (len(list1)):
    for j in range (len(list2)):
        var3=list1[i]+list2[j]
        list3.append(var3)

print(list1)
print(list2)
print(list3)
path=k+list3[0]
print(path)
imgx=cv2.imread(path)
cv2.imshow('img',imgx)
cv2.waitKey(0)
#encoded_face_train = findEncodings(list1)


#code to add attendance to the database according to the id sent as match
# def markAttendance(ID):
#     pass


#### take pictures from device
##cap  = cv2.VideoCapture("http://192.168.32.74:4747/video?640x480")
##while True:
##    success, img = cap.read()
##    if success:
##        imgS = cv2.resize(img, (0,0), None, 0.25,0.25)
##        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
##        faces_in_frame = face_recognition.face_locations(imgS)
##        encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
##        for encode_face, faceloc in zip(encoded_faces,faces_in_frame):
##            matches = face_recognition.compare_faces(encoded_face_train, encode_face)
##            faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
##            matchIndex = np.argmin(faceDist)
##            print(matchIndex)
##            if matches[matchIndex]:
##                name="debasmita"
##                #iD = classID[matchIndex]
##                y1,x2,y2,x1 = faceloc
##                # since we scaled down by 4 times
##                y1, x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
##                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
##                cv2.rectangle(img, (x1,y2-35),(x2,y2), (0,255,0), cv2.FILLED)
##                cv2.putText(img,name, (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
##                #call mark attendance
##                #markAttendance(iD)
##                
##        cv2.imshow('webcam', img)
##        if cv2.waitKey(1) & 0xFF == ord('q'):
##            break
##    else:
##         print("No image detected. Please! try again")
##
##
##
##
