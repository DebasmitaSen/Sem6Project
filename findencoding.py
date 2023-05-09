import cv2
import face_recognition
import numpy as np
import image_manupulation

def find_encoding():
    arrays = image_manupulation.retrive()
    classID=arrays[0]
    names=arrays[1]
    images=arrays[2]
    name2=[]
    classid=[]
    for i in range(len(names)):
        for j in range(5):
            name2.append(names[i])
            classid.append(classID[i])

    list1 = images
    var="/img"
    list2=[]
    list3=[]
    for i in  range (1,6):
        cn="%s"%i
        var2=var+cn+".jpg"
        list2.append(var2)
    for i in range (len(list1)):
        for j in range (len(list2)):
            var3=list1[i]+list2[j]
            list3.append(var3)
    imagelist=[]

    for i in range(len(names) * 5):
        path=list3[i]
        imgx=cv2.imread(path)
        imagelist.append(imgx)

    def findEncodings(image):
        encodeList = []
        for img in image:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    
            encoded_face = face_recognition.face_encodings(img)[0]
            encodeList.append(encoded_face)
        return encodeList


    encoded_face_train = findEncodings(imagelist)
    return name2, classid, encoded_face_train