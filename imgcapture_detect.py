import cv2 

#ip = input("IP address of device: ")
vid = cv2.VideoCapture("http://192.168.244.100:4747/video?640x480")
result,image=vid.read()
if result:

    # showing result, it take frame name and image
    # output
    imggray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("img1", imggray)

    # saving image in local storage
    
    cv2.imwrite("img1.png", imggray)

    # If keyboard interrupt occurs, destroy image
    # window
    cv2.waitKey(0)
    cv2.destroyWindow("img1")

# If captured image is corrupted, moving to else part
else:
    print("No image detected. Please! try again")
