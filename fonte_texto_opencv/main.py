import cv2
import numpy as np

img=np.zeros((320,600),dtype=np.uint8)
cv2.putText(img,"FONT_HERSHEY_SIMPLEX",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,255)
cv2.putText(img,"FONT_HERSHEY_COMPLEX",(10,60),cv2.FONT_HERSHEY_COMPLEX,1,255)
cv2.putText(img,"FONT_HERSHEY_DUPLEX",(10,90),cv2.FONT_HERSHEY_DUPLEX,1,255)
cv2.putText(img,"FONT_HERSHEY_TRIPLEX",(10,120),cv2.FONT_HERSHEY_TRIPLEX,1,255)

cv2.putText(img,"FONT_HERSHEY_COMPLEX_SMALL",(10,150),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,255)
cv2.putText(img,"FONT_HERSHEY_PLAIN",(10,180),cv2.FONT_HERSHEY_PLAIN,1,255)
cv2.putText(img,"FONT_HERSHEY_SCRIPT_COMPLEX",(10,210),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,255)

cv2.putText(img,"FONT_ITALIC",(10,240),cv2.FONT_ITALIC,1,255)
cv2.putText(img,"QT_FONT_BLACK",(10,270),cv2.QT_FONT_BLACK,1,255)
cv2.putText(img,"QT_FONT_NORMAL",(10,300),cv2.QT_FONT_NORMAL,1,255)

cv2.imshow("janela",img)
cv2.imwrite("fonte_opencv.jpg",img)
cv2.waitKey(0)