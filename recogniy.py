import cv2
import dlib
import face_recognition
import numpy as np

#code to connect to database and collect images and the id of student
#array name must be 'images'
#array for id must be 'classID'


def findEncodings(img):
    encodeList = []
#    for img in images:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encoded_face = face_recognition.face_encodings(img)[0]
    encodeList.append(encoded_face)
    return encodeList
image=cv2.imread("G:/Debasmita files/project/sample.jpg")
encoded_face_train = findEncodings(image)


#code to add attendance to the database according to the id sent as match
def markAttendance(ID):
    pass


# take pictures from device
cap  = cv2.VideoCapture("http://192.168.32.74:4747/video?640x480")
while True:
    success, img = cap.read()
    if success:
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
                name="debasmita"
                #iD = classID[matchIndex]
                y1,x2,y2,x1 = faceloc
                # since we scaled down by 4 times
                y1, x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img, (x1,y2-35),(x2,y2), (0,255,0), cv2.FILLED)
                cv2.putText(img,name, (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                #call mark attendance
                #markAttendance(iD)
                
        cv2.imshow('webcam', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
         print("No image detected. Please! try again")



