"""
边缘保留滤波（美颜）EPF
*相邻像素差异很大的时候（边缘），就不进行模糊操作，保留边缘。
1.高斯双边（高斯磨皮）
2.均值迁徙（边缘的时候会过度模糊，后续可以考虑边缘恢复加强）

"""

import numpy as np
import cv2 as cv

img_path = '.\static\example.png'


# 高斯双边
def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 15)  # 由后面两个参数反算倒数第三个
    # 以下为高斯模糊，效果很差
    # dst = cv.GaussianBlur(image, (0, 0), 5)
    cv.imshow('bi_demo', dst)


# 均值迁徙
def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)

    cv.imshow('shift_demo', dst)


def main():
    src = cv.imread(img_path)
    cv.namedWindow('img', cv.WINDOW_AUTOSIZE)
    cv.imshow('img', src)

    begin_time = cv.getTickCount()

    # bi_demo(src)

    shift_demo(src)

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time)/cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()