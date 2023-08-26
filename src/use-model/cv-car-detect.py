import cv2
import time
import numpy as np

# Create our body classifier
car_classifier = cv2.CascadeClassifier('/media/two-asus/Two2/AIT/DLCV/DLCV-Lab/assignment-1/ref/Computer-Vision-Tutorial/Haarcascades/haarcascade_car.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('/media/two-asus/Two2/AIT/DLCV/DLCV-Lab/assignment-1/video/video1.mp4')

# Create a named window with the specified flag
cv2.namedWindow('Cars', cv2.WINDOW_NORMAL)

frame_number = 0


# Loop once video is successfully loaded
while cap.isOpened():
    
    time.sleep(.05)
    # Read first frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
    # Pass frame to our car classifier
    cars = car_classifier.detectMultiScale(gray, 1.4, 2)
    
    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in cars:
        # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        # car = frame[y:y+h, x:x+w]
        
        cv2.imshow('Cars', frame)
        
        
        # Save the frame as an image
        frame_number += 1
        image_filename = f'/media/two-asus/Two2/AIT/DLCV/DLCV-Lab/assignment-1/images/frame_{frame_number}.jpg'
        cv2.imwrite(image_filename, frame)

    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()