"""
色彩空间 ：
1.色彩空间的转换
2.学会使用inRange
3.通道分离合并
"""

import numpy as np
import cv2 as cv

img_path = '.\static\cat.png'
video_path = r'.\static\video.wmv'


# 四个色彩空间转换 重要！！
def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow('COLOR_BGR2GRAY', gray)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)  # 常用
    cv.imshow('COLOR_BGR2HSV', hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)  # 常用
    cv.imshow('COLOR_BGR2YUV', yuv)
    Ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow('COLOR_BGR2YCrCb', Ycrcb)


# 学会使用inRange
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
        cv.imshow('video', hsv)
        cv.imshow('mask', mask)

        c = cv.waitKey(40)
        if c == 27:
            break


# 通道的分离合并
def image_split_demo(image):

    b, g, r = cv.split(image)
    """
    cv.imshow('blue', b)
    cv.imshow('green', g)
    cv.imshow('red', r)
    """
    # 单通道为0
    image[:, :, 2] = 0
    # cv.imshow('image', image)
    # 合并
    image = cv.merge([b, g, r])
    cv.imshow('image', image)


def main():
    src = cv.imread(img_path)
    cv.namedWindow('cat img', cv.WINDOW_AUTOSIZE)
    cv.imshow('cat img', src)

    begin_time = cv.getTickCount()

    # color_space_demo(src)
    # extrace_object_demo()
    image_split_demo(src)

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time)/cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
