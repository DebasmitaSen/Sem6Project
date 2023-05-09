import cv2
import dlib
from imutils import face_utils

# load the face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# set the pixel intensity threshold below which a blink is detected
PIXEL_THRESHOLD = 40

# initialize the frame counter and blink status
frame_count = 0
blink = False

# start the video stream
# cap = cv2.VideoCapture(0)
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

        # compute the average pixel intensity value for each eye
        left_eye_avg = gray[left_eye[:, 1], left_eye[:, 0]].mean()
        right_eye_avg = gray[right_eye[:, 1], right_eye[:, 0]].mean()

        # check if the pixel intensity value is below the threshold
        if left_eye_avg < PIXEL_THRESHOLD or right_eye_avg < PIXEL_THRESHOLD:
            # increment the frame counter
            frame_count += 1

            # check if the blink is complete
            if frame_count >= 3:
                blink = True

        # else:
        #     # reset the frame counter and blink status
        #     frame_count = 0
        #     blink = False

        # draw the eyes on the frame
        cv2.drawContours(frame, [cv2.convexHull(left_eye)], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [cv2.convexHull(right_eye)], -1, (0, 255, 0), 1)

        # check if the face is real
        if blink:
            cv2.putText(frame, "Real Face Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            cv2.putText(frame, "Fake Face Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # display the resulting frame
    cv2.imshow("Face Recognition", frame)

    # check if the 'q' key was pressed to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video stream and close all windows
cap.release()
cv2.destroyAllWindows()