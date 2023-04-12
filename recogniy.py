import cv2
import dlib
import face_recognition
import numpy as np
import connection
import attendence


#code to connect to database and collect images and the id of student
#array name must be 'images'
#array for id must be 'classID'
def getArray():
    arrays = connection.retrive()
    classID=arrays[0]
    names=arrays[1]
    images=arrays[2]
    name1=names
    cid=classID
    name2=[]
    classid=[]
    for i in range(len(name1)):
        for j in range(5):
            name2.append(name1[i])
            classid.append(cid[i])
    data=[images,name2,classid]
    return data 

def findEncodings(image):
    encodeList = []
    for img in image:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    
        encoded_face = face_recognition.face_encodings(img)[0]
        encodeList.append(encoded_face)
    return encodeList


def createImg():
    getdata=getArray()
    list1=getdata[0]
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

    for i in range(15):
        path=list3[i]
        imgx=cv2.imread(path)
        imagelist.append(imgx)


    encoded_face_train = findEncodings(imagelist)
    return encoded_face_train



###### take pictures from device
def recogniseImg():
    # cap  = cv2.VideoCapture("http://100.81.178.96:4747/video?640x480")
    cap  = cv2.VideoCapture(0)
    getdata1=getArray()
    name2=getdata1[1]
    classid=getdata1[2]
    encoded_face_train=createImg()
    while True:
        success, img = cap.read()
        if not success:
            break
        else:           
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
                    y1,x2,y2,x1 = faceloc
                    # since we scaled down by 4 times
                    y1, x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                    cv2.rectangle(img, (x1,y2-35),(x2,y2), (0,255,0), cv2.FILLED)
                    cv2.putText(img,"Detected", (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    #call mark attendance
                    # attendence.markAttendance(iD)
                    print(iD, name)
                else:
                    y1,x2,y2,x1 = faceloc
                    # since we scaled down by 4 times
                    y1, x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                    cv2.rectangle(img, (x1,y2-35),(x2,y2), (0,255,0), cv2.FILLED)
                    cv2.putText(img,"Unrecognizable", (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,0.50,(0,0,255),2)
                # return (iD, name)
            cv2.imshow('webcam', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
              
           
            
    
    cap.release()



recogniseImg()
