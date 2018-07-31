#!/usr/bin/python3
# coding=utf-8

import cv2 as cv

img=cv.imread("yong.jpg")

cv.imshow("who",img)

cv.waitKey(0)

cv.destroyAllWindows()