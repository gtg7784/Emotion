import cv2
import sys
import datetime
import os

capture = cv2.VideoCapture(0)  # 0 is for /dev/video0

while True:
    ret, frame = capture.read()
    
    if ret == True:
        cv2.imshow('frame', frame)

    key = cv2.waitKey(1);

    if key == ord('q'):
        break

    elif key == ord('s'):
      for i in range(1000):
        name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
        path = os.path.join('./', 'train', 'gtg', name)
        cv2.imwrite(path, frame)
        print(path, 'saved')

capture.release()
cv2.destroyAllWindows()