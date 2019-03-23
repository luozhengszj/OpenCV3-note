"""
直方图反向投影

"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img_path = '.\static\lena.png'
c_img_path = '.\static\c.png'
ctarget_img_path = '.\static\c_target.png'


def hist2d_demo(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    # [180, 180]直方图的bin大小
    hist = cv.calcHist([image], [0, 1], None, [60, 60], [0, 180, 0, 256])
    # cv.imshow('hist2d', hist)
    plt.imshow(hist, interpolation='nearest')
    plt.show()


# 直方图反向投影，直方图格子的大小
def back_project():
    c = cv.imread(c_img_path)
    c_target = cv.imread(ctarget_img_path)
    target_hsv = cv.cvtColor(c_target, cv.COLOR_BGR2HSV)
    roi_hsv = cv.cvtColor(c, cv.COLOR_BGR2HSV)

    # show images
    cv.imshow("c", c)
    cv.imshow("c_target", c_target)

    # [36, 48] bin的大小
    target_Hist = cv.calcHist([target_hsv], [0, 1], None, [18, 18], [0, 180, 0, 256])
    cv.normalize(target_Hist, target_Hist, 0, 255, cv.NORM_MINMAX)
    dst = cv.calcBackProject([roi_hsv], [0, 1], target_Hist, [0, 180, 0, 256], 1)
    cv.imshow('back_project',dst)

    # 结果与全图与操作 and


def main():
    # src = cv.imread(img_path)
    # cv.namedWindow('lena img', cv.WINDOW_AUTOSIZE)
    # cv.imshow('lena img', src)

    begin_time = cv.getTickCount()

    # hist2d_demo(src)

    back_project()

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time)/cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
