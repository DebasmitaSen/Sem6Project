import cv2
import dlib
from scipy.spatial import distance as dist
from imutils import face_utils

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# load the face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# set the EAR threshold below which a blink is detected
EAR_THRESHOLD = 0.2

# initialize the frame counter and blink status
frame_count = 0
blink = False

# start the video stream
cap  = cv2.VideoCapture("http://100.70.121.122:4747/video?640x480")


while True:
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

        # extract the left and right eye coordinates
        left_eye = shape[42:48]
        right_eye = shape[36:42]

        # compute the EAR for each eye
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)

        # compute the average EAR for both eyes
        ear = (left_ear + right_ear) / 2.0

        # check if the EAR is below the threshold
        if ear < EAR_THRESHOLD:
            # increment the frame counter
            frame_count += 1

            # check if the blink is complete
            if frame_count >= 3:
                blink = True

        else:
            # reset the frame counter and blink status
            frame_count = 0
            blink = False

        # draw the eyes and EAR on the frame
        cv2.drawContours(frame, [cv2.convexHull(left_eye)], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [cv2.convexHull(right_eye)], -1, (0, 255, 0), 1)
        cv2.putText(frame, "EAR: {:.2f}".format(ear), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # check if a blink is detected
        if blink:
            cv2.putText(frame, "Blink Detected", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # show the frame
    cv2.imshow("Frame", frame)

    # check for key press to exit
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# release the video stream and close all windows
cap.release()
cv2.destroyAllWindows()