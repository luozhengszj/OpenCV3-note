"""
图像梯度
1.一阶导数和Sobel算子、Scharr算子
2.二阶倒数和Laplacian算子、自定义拉普拉斯算子

"""

import cv2 as cv
import numpy as np

lena_img_path = r'.\static\lena.png'


def soble_demo(image):
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    # x,y方向的梯度差异分别展示
    cv.imshow('gradx', gradx)
    cv.imshow('grady', grady)
    # x,y梯度方向差异合并
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow('gradxy', gradxy)


# Scharr算子是Sobel算子的增强版，当使用Sobel算子得到的线条不明显，可以考虑Scharr算子
def scharr_demo(image):
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)
    grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    # x,y方向的梯度差异分别展示
    cv.imshow('gradx', gradx)
    cv.imshow('grady', grady)
    # x,y梯度方向差异合并
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow('gradxy', gradxy)


# 拉普拉斯算子
def laplacian_demo(image):
    # 本身的api
    dst = cv.Laplacian(image, cv.CV_32F)
    # 变为单通道图像
    lpls = cv.convertScaleAbs(dst)
    cv.imshow('lpls', lpls)


# 自定义拉普拉斯算子
def laplacian_sp_demo(image):
    # 自定义拉普拉斯[4,0,1]算子（拉普拉斯默认算子）
    # kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    # 自定义拉普拉斯[8,0,1]算子
    kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    dst = cv.filter2D(image, cv.CV_32F, kernel=kernel)
    # 变为单通道图像
    lpls = cv.convertScaleAbs(dst)
    cv.imshow('lpls', lpls)


def main():

    src = cv.imread(lena_img_path)
    cv.namedWindow('lena img', cv.WINDOW_AUTOSIZE)
    cv.imshow('lena img', src)

    begin_time = cv.getTickCount()

    # soble_demo(src)

    # scharr_demo(src)

    # laplacian_demo(src)
    laplacian_sp_demo(src)

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time)/cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()