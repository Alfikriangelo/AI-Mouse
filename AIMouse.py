import cv2 
import numpy as np
import HandTrackingModule as htm
import time
import autopy

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
cTime = 0




while True:
    # 1. find hand landmarks
    success, img = cap.read()

    # 2. get the tip of the index and middle fingers
    # 3. check which fingers are up
    # 4. only index finger : moving mode
    # 5. convert coordinates
    # 6. smoothen values
    # 7. move mouse
    # 8. both index and middle fingers are up : clicking mode
    # 9. find distance between fingers
    # 10. click mouse if distance short


    # 11. frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(
        img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3
    )

    # 12. display
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        

