import cv2
import face_recognition
import numpy as np
import image_manupulation
import attendence
import cv2
import dlib
from imutils import face_utils
import findencoding

#code to connect to database and collect images and the id of student
#array name must be 'images'
#array for id must be 'classID'

name2=[]
classid=[]
encoded_face_train = []

def face_train():
    global encoded_face_train
    global name2
    global classid

    name2, classid, encoded_face_train = findencoding.find_encoding()

face_train()

# initialize dlib's face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

###### take pictures from device
def recogniseImg(cap):

    MAX_HEAD_UP = 5
    MAX_HEAD_DOWN = -5
    c=0

    success, img = cap.read()
    if not success:
        print("Unable to access camera")
    else: 
        # convert the frame to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)

        x=0.5          
        imgS = cv2.resize(img, (0,0), None, 0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        faces_in_frame = face_recognition.face_locations(imgS)
        encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
        for encode_face, faceloc in zip(encoded_faces,faces_in_frame):
            matches = face_recognition.compare_faces(encoded_face_train, encode_face)
            faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
            print(faceDist)
            if (faceDist < x).any():
                matchIndex = np.argmin(faceDist)
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
                        
                    for rect in rects:
                        # extract the face landmarks
                        shape = predictor(gray, rect)
                        shape = face_utils.shape_to_np(shape)

                        # extract the coordinates for the eyes, nose, and mouth
                        left_eye = shape[36:42]
                        right_eye = shape[42:48]
                        nose = shape[27]
                        mouth_left = shape[48]
                        mouth_right = shape[54]

                        # compute the centroid of the eyes, nose, and mouth
                        eye_centroid = ((left_eye.sum(axis=0) + right_eye.sum(axis=0)) / 12).astype(int)
                        nose_centroid = nose
                        mouth_centroid = ((mouth_left + mouth_right) / 2).astype(int)

                        # compute the angle between the eyes, nose, and mouth
                        angle_up_down = -(eye_centroid[1] - nose_centroid[1])
                        
                            
                        # check if the head movement exceeds the threshold angles
                        if angle_up_down > MAX_HEAD_UP or angle_up_down < MAX_HEAD_DOWN :
                            c=c+1


                    if c>0:
                        print(iD, name)
                        attendence.markAttendance(iD)
                        return iD
            else:
                return 0