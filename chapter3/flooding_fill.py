"""
ROI(Region of onterest) 和 泛洪填充
1.图像的矩形提取：numpy提取
2.泛洪填充demo（改变图像，泛洪填充）
3.二值图像填充（不改变图像，只对遮罩层本身进行填充）
"""

import numpy as np
import cv2 as cv

img_path = '.\static\cat.png'


def rectangular_operate(image):
    face = image[50:250, 100:300]  # 提取图像的左上角点和右下角点（得到矩形）
    gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
    backface = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
    image[50:250, 100:300] = backface
    # cv.imshow('gray', gray)
    cv.imshow('image', image)


def fill_color_demo(image):
    coypImage = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)

    # 从(30, 30)为当前标准像素点x，x-(100, 100, 100)为最低像素点-，x+(50, 50, 50)最高像素点
    cv.floodFill(coypImage, mask, (30, 30), (0, 255, 255), (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow('floodFill', coypImage)


def fill_binary():
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, :] = 255
    cv.imshow('image', image)

    # 以上图片的区域进行填充 （红色）
    # 由于使用FLOODFILL_MASK_ONLY，所以不为1的区域（mask）才会填充。所以需要先对mask全部初始化为1，填充的区域全部初始化为0
    mask = np.ones([402, 402, 1], np.uint8)
    mask[101:301, 101:301] = 0
    cv.floodFill(image, mask, (200, 200), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow('fill_binary', image)


def main():
    src = cv.imread(img_path)
    cv.namedWindow('cat img', cv.WINDOW_AUTOSIZE)
    cv.imshow('cat img', src)

    begin_time = cv.getTickCount()

    # rectangular_operate(src)

    # fill_color_demo(src)

    fill_binary()

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time)/cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
