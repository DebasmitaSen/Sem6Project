import cv2

# Open the video file
cap = cv2.VideoCapture(0)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error opening video file")

# Initialize a variable to keep track of the number of frames captured
frame_count = 0
id=input("Enter ID: ")
name=input("Enter Name: ")
# Loop through the frames of the video
while cap.isOpened() and frame_count < 10:
    # Read the next frame from the video
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        break

    # Display the current frame (optional)
    cv2.imshow('frame', frame)

    # Save the current frame to a file
    cv2.imwrite(f'Input/{name}_{id}_{frame_count}.jpg', frame)

    # Increment the frame count
    frame_count += 1

    # Wait for a key press to exit (optional)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video file and close all windows
cap.release()
cv2.destroyAllWindows()
