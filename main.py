import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import random
detector=HandDetector(detectionCon=0.8, maxHands=2)

video=cv2.VideoCapture(1)

def function(timer):
        prev=time.time()
        while timer>=0:
            ret,frame=video.read()
            cv2.rectangle(frame, (0,0), (280, 50), (0,0,0), -2, cv2.LINE_AA)
            cv2.putText(frame, 'Timer : {}'.format(str(timer)), (20,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (50,50,255), 2)
            cv2.imshow('frame', frame)
            cv2.waitKey(100)
            cur=time.time()
            if cur-prev>1:
                prev=cur
                timer = timer - 1
        else:
            ret,frame=video.read()
            cv2.imshow('frame', frame)
            cv2.waitKey(1000)
            cv2.imwrite('camera{}.jpg'.format(random.randint(1,1000)), frame)

while True:
    ret, frame=video.read()
    hands, _ = detector.findHands(frame)
    if hands:
        hands1=hands[0]
        fingercount = detector.fingersUp(hands1)
        print(fingercount)
        if fingercount==[0,0,0,0,0]:
            # function(int(0))
            pass
        if fingercount==[0,1,0,0,0]:
            function(int(1))
        if fingercount==[0,1,1,0,0]:
            function(int(2))
        if fingercount==[0,1,1,1,0]:
            function(int(3))
        if fingercount==[0,1,1,1,1]:
           function(int(4))
        if fingercount==[1,1,1,1,1]:
            function(int(5))
    cv2.imshow('frame', frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
video.release()
cv2.destroyAllWindows()