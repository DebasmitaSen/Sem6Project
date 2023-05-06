import cv2
import face_recognition
import numpy as np
import image_manupulation
import attendence


#code to connect to database and collect images and the id of student
#array name must be 'images'
#array for id must be 'classID'
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


def findEncodings(image):
    encodeList = []
    for img in image:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    
        encoded_face = face_recognition.face_encodings(img)[0]
        encodeList.append(encoded_face)
    return encodeList



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


encoded_face_train = findEncodings(imagelist)



###### take pictures from device
def recogniseImg(cap):

    success, img = cap.read()
    if not success:
        print("unable to access camera")
    else: 
        iD = ''          
        imgS = cv2.resize(img, (0,0), None, 0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        faces_in_frame = face_recognition.face_locations(imgS)
        encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
        for encode_face, faceloc in zip(encoded_faces,faces_in_frame):
            matches = face_recognition.compare_faces(encoded_face_train, encode_face)
            faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
            matchIndex = np.argmin(faceDist)
            print(matchIndex)               
            if matches[matchIndex]:                   
                name= name2[matchIndex]
                iD = classid[matchIndex]
                #call mark attendance
                attendence.markAttendance(iD)
                print(iD, name)
                return (iD)
            else:
                return (iD)
