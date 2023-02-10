import cv2
import time
video=cv2.VideoCapture(0)

timer=int(5)

while True:
    ret, frame=video.read()
    cv2.imshow('frame', frame)
    k=cv2.waitKey(1)
    if k==ord('t'):
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
            cv2.imwrite('camera.jpg', frame)
    if k==ord('q'):
        break

video.release()
cv2.destroyAllWindows()