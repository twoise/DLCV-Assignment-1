import cv2

counter = 0

# rtsp://admin:pass@10.43.64.134/rtsph2641080p

camera_url = "rtsp://admin:pass@10.43.64.134/rtsph2641080p"

cap = cv2.VideoCapture(camera_url)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()
    
while True:
    ret, frame = cap.read()
    counter += 1
    
    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow('IP Camera', frame)
    
    image_filename = "/media/two-asus/Two3/AIT/DLCV/DLCV-Lab/assignment-1/images/image-ipcam/captured_image{}.jpg".format(counter)
    cv2.imwrite(image_filename, frame)
    print(f"Image saved as {image_filename}")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()