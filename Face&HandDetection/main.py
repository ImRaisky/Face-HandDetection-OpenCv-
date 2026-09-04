from pathlib import Path
import cv2 as cv
import mediapipe as mp

BASE_DIR = Path(__file__).resolve().parent
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

Face_Cascade = cv.CascadeClassifier(str(BASE_DIR / "haar_face.xml"))



video = cv.VideoCapture(0)

while True:
    ret, img = video.read()
    if ret:
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # Face Detecting

        faces_rect = Face_Cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

        for (x,y,w,h) in faces_rect:
            cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)


        # hand detecting
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


        cv.imshow("Raisky Hand Pose Estimator", img)
    q = cv.waitKey(1)
    if q == ord("q"):
        break
