"""
开操作：先腐蚀再膨胀，主要作用：去噪点，去掉小的干扰块
闭操作：先膨胀再腐蚀，主要作用：填充小的封闭区域
其他作用：水平或垂直直线提取、干扰线的去除

1.块的大小影响去噪的噪点大小(5, 5)
"""

import cv2 as cv

morph_img_path = r'.\static\morph.png'
morph01_img_path = r'.\static\morph01.png'
morph02_img_path = r'.\static\morph02.png'


# 开操作：去掉了图片的噪点
def open_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    # 块的大小影响去噪的噪点大小(5, 5)
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    cv.imshow("open-result", binary)


# 闭操作：去掉了四边形里面的黑点
def close_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
    cv.imshow("close_demo", binary)


# 去掉水平或垂直的线
def remove_horizontal_line_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    # kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 15))  # 去掉水平的线
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 1))  # 去掉垂直的线
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    cv.imshow("open-result", binary)


# 去掉水平或垂直的线
def remove_interference_line_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  # 去掉干扰的线
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    cv.imshow("open-result", binary)


def main():
    # src = cv.imread(morph_img_path)
    # src = cv.imread(morph01_img_path)
    src = cv.imread(morph02_img_path)
    cv.namedWindow('img', cv.WINDOW_AUTOSIZE)
    cv.imshow('img', src)

    begin_time = cv.getTickCount()

    # open_demo(src)

    # close_demo(src)

    # remove_horizontal_line_demo(src)

    remove_interference_line_demo(src)

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time) / cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()


