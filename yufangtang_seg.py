# -*- coding:gbk -*-
import cv2
import numpy as np
from aip import AipOcr


def seg(image_path):
    image = cv2.imread(image_path)
    img = cv2.GaussianBlur(image,(5,5),0)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    mask = np.zeros((gray.shape),np.uint8)
    kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))

    close = cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel1)
    div = np.float32(gray)/(close)
    res = np.uint8(cv2.normalize(div,div,0,255,cv2.NORM_MINMAX))
    res2 = cv2.cvtColor(res,cv2.COLOR_GRAY2BGR)

    thresh = cv2.adaptiveThreshold(res,255,0,1,19,2)
    ret,thresh = cv2.threshold(res,225,255,cv2.THRESH_BINARY_INV)
    kernel = np.ones((3, 10), np.uint8)
    thresh = cv2.dilate(thresh, kernel, iterations=2)


    # contour = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    binary, contour, hierarchy = cv2.findContours(thresh, 1, cv2.CHAIN_APPROX_SIMPLE)


    max_area = 0
    best_cnt = None
    for cnt in contour:
        area = cv2.contourArea(cnt)
        if area > 1000:
            if area > max_area:
                max_area = area
                best_cnt = cnt

    mask = cv2.drawContours(mask,[best_cnt],0,255,-1)

    # cv2.drawContours(mask,[best_cnt],0,0,2)


    kernel = np.ones((3, 10), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=2)
    kernel = np.ones((10, 1), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=3)

    img, contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0
    best_cnt = None
    for con in contours:
        area = cv2.contourArea(con)
        if area > max_area:
            max_area = area
            x, y, w, h = cv2.boundingRect(con)
            top = y
            bottow = y + h
            left = x
            right = x + w
    img1 = image[0:top, 0:len(img[0])]
    img2 = image[top:bottow, 0:right]
    img3 = image[top:bottow, right:len(img[0])]
    cv2.imwrite('img1.jpg',img1)
    cv2.imwrite('img2.jpg',img2)
    cv2.imwrite('img3.jpg',img3)
# cv2.namedWindow('img1', 0)
# cv2.resizeWindow('img1', 600, 900)
# cv2.imshow('img1', img1)
    cv2.waitKey(0)
