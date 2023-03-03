import cv2
import numpy as np

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
img = cv2.VideoCapture(0)

while True:
    ret, frame = img.read()
    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_detections = face_detector.detectMultiScale(image_gray )

    for (x, y, w, h) in face_detections:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)

    eyes_detections = eye_detector.detectMultiScale(image_gray)

    for (x, y, w, h) in eyes_detections:
       cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 225), 5)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

img.release()
cv2.destroyAllWindows()
