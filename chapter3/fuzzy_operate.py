"""
图像模糊操作（数学离散卷积知识）
一、模糊基本步骤：
1.基于离散卷积
2.定义好每个卷积核
3.不同的卷积核得到不同的卷积效果
3.模糊是卷积的一种表象
二、卷积原理
如图一维卷积。
一维卷积的时候，目前是步长3，边缘有2个像素未被处理（左右两边）；若步长为5，边缘有4个像素未被处理（左右两边）。
二维卷积则是步骤3*3地走。
三、demo
1.均值模糊（随机噪声）
2.中值模糊（椒盐噪声）
3.自定义模糊
  锐化 下面的kernel是锐化算子 [1.奇数，2.总和=1或=0，3.=0可能是在做边缘的梯度性，=1可能在做增强图像 ]

"""

import numpy as np
import cv2 as cv

img_path = '.\static\lenanoise.png'


def blur_demo(image):
    # (15, 1)水平方向模糊15 ， (1, 15)垂直方向模糊15
    dst = cv.blur(image, (15, 1))
    cv.imshow('blur_demo', dst)


def median_demo(image):
    # (15, 1)水平方向模糊15 ， (1, 15)垂直方向模糊15
    dst = cv.medianBlur(image, 3)
    cv.imshow('median_demo', dst)


def custom_blur_demo(image):
    # /25保证不溢出
    # kernel = np.ones([5, 5], np.float32)/25

    # kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], np.float32) / 9

    # 锐化 下面的kernel是锐化算子 [1.奇数，2.总和=1或=0，3.=0可能是在做边缘的梯度性，=1可能在做图像的增强（立体感、轮廓等） ]
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    dst = cv.filter2D(image, -1, kernel = kernel)
    cv.imshow('custom_blur_demo', dst)


def main():
    src = cv.imread(img_path)
    cv.namedWindow('img', cv.WINDOW_AUTOSIZE)
    cv.imshow('img', src)

    begin_time = cv.getTickCount()

    # blur_demo(src)

    # median_demo(src)

    custom_blur_demo(src)

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time)/cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
