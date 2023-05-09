import cv2
import dlib
from imutils import face_utils

# initialize dlib's face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# initialize the video capture object
cap = cap  = cv2.VideoCapture("http://100.70.121.122:4747/video?640x480")


# define the threshold angles for head movement
MAX_HEAD_UP = 5
MAX_HEAD_DOWN = -5
MAX_HEAD_LEFT = -5
MAX_HEAD_RIGHT = 5
x=0
c=0
movhead=[]
while (x<20):
    # read a frame from the video stream
    ret, frame = cap.read()

    # convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale frame
    rects = detector(gray, 0)

    # loop over the face detections
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
        angle_left_right = eye_centroid[0] - mouth_centroid[0]
        print(angle_up_down)
        
        # check if the head movement exceeds the threshold angles
        if angle_up_down > MAX_HEAD_UP or angle_up_down < MAX_HEAD_DOWN :
            c=c+1
            # print("Head movement detected! This is a real person.")
            movhead.append(c)
        # else:
        #     print("No head movement detected. This may not be a real person.")

    # show the video stream
    cv2.imshow("Head Movement Detection", frame)
    x=x+1
   

    # exit if 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# release the video capture object and close all windows
if c>0:
     print("real person")
cap.release()
cv2.destroyAllWindows()