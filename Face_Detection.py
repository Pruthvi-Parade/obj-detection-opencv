import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# This is the code for an image / (to detect faces from a image)

# img = cv2.imread('test.jpeg')

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# cv2.imshow('img', img)
# cv2.waitKey()

# This is the code for video capture 

# cap = cv2.VideoCapture(0)  # 0 is for the webcam
cap = cv2.VideoCapture('test.mp4')

while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()