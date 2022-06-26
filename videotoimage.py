import numpy as np
import cv2
cap = cv2.VideoCapture(r'D:\Saaswath\monday projects\human posture Identifiaction\Meena Lotchani-20220515T080510Z-001\Meena Lotchani\Video Capture posture\Normal.mp4')
i = 0
while(cap.isOpened()):
  ret, frame = cap.read()
  #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  if ret == False:
     break
  cv2.imwrite('D:/Saaswath/monday projects/human posture Identifiaction/Jyotsna/train/Frame'+str(i)+'.jpg', frame)
  i += 1


cap.release()
cv2.destroyAllWindows()