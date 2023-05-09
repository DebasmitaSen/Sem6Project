import cv2

def imcapture(id, name, cap):

    # Check if the video file was opened successfully
    if not cap.isOpened():
        print("Error opening video file")

    # Initialize a variable to keep track of the number of frames captured
    frame_count = 1

    while cap.isOpened() and frame_count < 6:
        # Read the next frame from the video
        ret, frame = cap.read()
        # Check if the frame was successfully read
        if not ret:
            break

        # Display the current frame (optional)
        cv2.imshow('frame', frame)

        # Save the current frame to a file
        cv2.imwrite(f'Input/{name}_{id}-{frame_count}.jpg', frame)

        # Increment the frame count
        frame_count += 1

