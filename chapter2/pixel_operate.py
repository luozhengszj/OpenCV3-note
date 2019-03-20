"""
图像像素运算：两个图像大小需要一致
1.加减乘除
2.均值（简单的图像信息统计）、方差（图片像素的差异）
3.逻辑运算（与或非）
4.与或非在图像提取的一个应用
5.图像的对比度、亮度
"""

import numpy as np
import cv2 as cv

black_img_path = r'.\static\black.png'
windows_img_path = r'.\static\windows.png'
video_path = r'.\static\video.wmv'
img_path = '.\static\cat.png'


def add_demo(image1, image2):
    dst = cv.add(image1, image2)
    cv.imshow('dst', dst)


def subtract_demo(image1, image2):
    dst = cv.subtract(image1, image2)
    cv.imshow('dst', dst)


def divide_demo(image1, image2):
    dst = cv.divide(image1, image2)
    cv.imshow('dst', dst)


def multiply_demo(image1, image2):
    dst = cv.multiply(image1, image2)
    cv.imshow('dst', dst)


def other(image1, image2):
    m1 = cv.mean(image1)
    m2 = cv.mean(image2)
    print(m1)
    print(m2)
    """
    三个通道的像素信息
    (162.6543918474688, 162.6543918474688, 162.6543918474688, 0.0)
    (185.19010519395135, 199.90382642998028, 207.90518080210387, 0.0)
    """

    m1 = cv.meanStdDev(image1)
    m2 = cv.meanStdDev(image2)
    print(m1)
    print(m2)
    """
    方差越大、对比度越大，图像像素的差别越大
    (array([[162.65439185],
       [162.65439185],
       [162.65439185]]), array([[120.04594522],
       [120.04594522],
       [120.04594522]]))
    (array([[185.19010519],
       [199.90382643],
       [207.9051808 ]]), array([[92.46519007],
       [72.60591752],
       [68.06761154]]))
    """

def logic_demo(image1, image2):
    # dst = cv.bitwise_and(image1, image2)
    # dst = cv.bitwise_or(image1, image2)
    dst = cv.bitwise_not(image1)
    cv.imshow('bitewise', dst)


# 与或非在图像提取的一个应用
def extrace_object_demo():
    capture = cv.VideoCapture(video_path)
    while 1:
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37, 43, 46])
        upper_hsv = np.array([77, 255, 255])
        mask = cv.inRange(hsv,lowerb = lower_hsv, upperb = upper_hsv)
        dst = cv.bitwise_and(frame, frame, mask = mask)
        cv.imshow('video', hsv)
        cv.imshow('mask', mask)
        cv.imshow('dst', dst)

        c = cv.waitKey(40)
        if c == 27:
            break


def contrast_brightness_demo(image, c, b):
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1-c, b)
    cv.imshow("con-bri-demo", dst)


def main():
    src = cv.imread(img_path)
    # black_img_src = cv.imread(black_img_path)
    # windows_img_src = cv.imread(windows_img_path)

    # cv.namedWindow('img1', cv.WINDOW_AUTOSIZE)
    # cv.imshow('black_img_src', black_img_src)
    # cv.imshow('windows_img_src', windows_img_src)

    begin_time = cv.getTickCount()

    # add_demo(black_img_src, windows_img_src)
    # subtract_demo(black_img_src, windows_img_src)
    # divide_demo(black_img_src, windows_img_src)
    # multiply_demo(black_img_src, windows_img_src)

    # other(black_img_src, windows_img_src)

    # logic_demo(black_img_src, windows_img_src)

    # extrace_object_demo()

    contrast_brightness_demo(src, 1.5, 0)  # 对比度，亮度

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time)/cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
