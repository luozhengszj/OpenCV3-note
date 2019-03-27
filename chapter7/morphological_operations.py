"""
其他形态学操作
1.顶帽 tophat:原图像与开操作之间的差值图像
2.黑帽 blackhat:闭操作与原图像的差值图像
3.其他形态学操作 Gradient
    1.基本梯度：膨胀后的图像减去腐蚀后的图像
    2.内部梯度：原图减去腐蚀图像的差值图像
    3.外部图像：膨胀图像减去原图的差值图像

"""

import numpy as np
import cv2 as cv

cat_img_path = r'.\static\cat.png'


# 图像的顶帽黑帽
def hat_gray_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (8, 8))
    # dst = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)    # 顶帽
    dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)  # 黑帽
    # 增加亮度
    cimage = 100;
    dst = cv.add(dst, cimage)
    cv.imshow('top_hat_democ', dst)


# 二值图像的顶帽、黑帽操作
def hat_binary_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dst = cv.morphologyEx(binary, cv.MORPH_BLACKHAT, kernel)
    cv.imshow("tophat", dst)


# 基本梯度
def basic_gradient_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dst = cv.morphologyEx(binary, cv.MORPH_GRADIENT, kernel)
    cv.imshow("tophat", dst)


# 内外梯度
def gradient_demo(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dm = cv.dilate(image, kernel)
    em = cv.erode(image, kernel)
    dst1 = cv.subtract(image, em)  # internal gradient
    dst2 = cv.subtract(dm, image)  # external gradient
    cv.imshow("internal", dst1)
    cv.imshow("external", dst2)


def main():
    src = cv.imread(cat_img_path)
    cv.namedWindow('img', cv.WINDOW_AUTOSIZE)
    cv.imshow('img', src)

    begin_time = cv.getTickCount()

    # hat_gray_demo(src)

    # hat_binary_demo(src)

    # basic_gradient_demo(src)

    gradient_demo(src)

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time) / cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
