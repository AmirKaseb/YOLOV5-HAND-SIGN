<<<<<<< HEAD
import cv2
import time
video = cv2.VideoCapture(0)
count=0
while True:
    ret,frame=video.read()
    count+=1
    name = './images/'+'No'+'/'+'No'+str(count)+'.jpg'
    cv2.imwrite(name,frame)
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    time.sleep(2)
    if count>20 or k==ord('q'):
        break
video.release()
=======
import cv2
import time
video = cv2.VideoCapture(0)
count=0
while True:
    ret,frame=video.read()
    count+=1
    name = './images/'+'No'+'/'+'No'+str(count)+'.jpg'
    cv2.imwrite(name,frame)
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    time.sleep(2)
    if count>20 or k==ord('q'):
        break
video.release()
>>>>>>> 037375efc49aff6436eb3c530b75c6bfa98c7648
cv2.destroyAllWindows()