import cv2
from cvzone.HandTrackingModule import HandDetector

w,h=1280,720;
cam = cv2.VideoCapture(0)
cam.set(3,w)
cam.set(4,h)

dec = HandDetector(maxHands=1,detectionCon=0.8)

while True:
    _,img = cam.read()
    han,img = dec.findHands(img)
    data = []
    if han:
        h = han[0]

        lmList = h['lmList']
        print(lmList)
       # for lm in lmList:
       #     data.extend([lm[0],h - lm[1],lm[2]])
        #print(data)

    cv2.imshow("vid",img)

    #cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


