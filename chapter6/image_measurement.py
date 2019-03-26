"""
图像测量
1.图像中心点
2.图像面积测量
3.图像线段逼近（根据逼近的线段数得出图像形状）

"""

import cv2 as cv
import numpy as np

int_img_path = r'.\static\7259.png'
contours_img_path = r'.\static\contours.png'


def measure_object(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # 有时候需要取反
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    print('threshold value: %s' % ret)
    cv.imshow('binary image', binary)

    contours, hireachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)
        x, y, w, h = cv.boundingRect(contour)
        mm = cv.moments(contour)
        print(type(mm))
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']
        cv.circle(image, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print('contour area is %s' % area)
    cv.imshow('measure_object', image)


# 图像宽高比等信息
def measure_object_info(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # 有时候需要取反
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    print('threshold value: %s' % ret)
    cv.imshow('binary image', binary)

    contours, hireachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)
        x, y, w, h = cv.boundingRect(contour)

        rate = min(w, h)/max(w, h)
        print("rectangle rate : %s"%rate)

        mm = cv.moments(contour)
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']
        cv.circle(image, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print('contour area is %s' % area)
    cv.imshow('measure_object', image)


# 多边形逼近
def measure_object_approach(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print("threshold value : %s"%ret)
    cv.imshow("binary image", binary)
    dst = cv.cvtColor(binary, cv.COLOR_GRAY2BGR)
    contours, hireachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)
        x, y, w, h = cv.boundingRect(contour)
        rate = min(w, h)/max(w, h)
        print("rectangle rate : %s"%rate)
        mm = cv.moments(contour)
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']
        cv.circle(dst, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)
        #cv.rectangle(dst, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print("contour area %s"%area)

        # 画图的线段数
        approxCurve = cv.approxPolyDP(contour,4, True)
        print(approxCurve.shape)
        if approxCurve.shape[0] > 6:   # 逼近直线>6条  多边形、圆形等
            cv.drawContours(dst, contours, i, (0, 255, 0), 2)
        if approxCurve.shape[0] == 4:    # 逼近直线=4条  四边形
            cv.drawContours(dst, contours, i, (0, 0, 255), 2)
        if approxCurve.shape[0] == 3:    # 逼近直线=3条  三角形
            cv.drawContours(dst, contours, i, (255, 0, 0), 2)
        if approxCurve.shape[0] == 6:    # 逼近直线=6条  六角形
            cv.drawContours(dst, contours, i, (100, 255, 255), 2)
    cv.imshow("measure-contours", dst)


def main():
    # src = cv.imread(int_img_path)
    src = cv.imread(contours_img_path)
    cv.namedWindow('img', cv.WINDOW_AUTOSIZE)
    cv.imshow('img', src)

    begin_time = cv.getTickCount()

    # measure_object(src)

    # measure_object_info(src)

    measure_object_approach(src)

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time) / cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
