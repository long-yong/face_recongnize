#!/usr/bin/python3
# coding=utf-8

import sys
import cv2

cap = cv2.VideoCapture(0)
i = 100

while(1):
    ret, frame = cap.read()
    cv2.imshow("capture", frame)
    if cv2.waitKey(10) & 0xFF == ord(' '):
        i += 1
        imgName = "img/" + str(i) + ".jpeg"
        cv2.imwrite(imgName, frame)
        print(imgName+' is saved!')
    if cv2.waitKey(10) & 0xFF == ord('q'):
        print('quit')
        break

cap.release()
cv2.destroyAllWindows()