"""
图像边缘提取：Canny边缘检测算法（对噪声敏感，所以先使用GaussianBlur除噪）
步骤：
1.高斯模糊GaussianBlur
2.灰度转换cvtColor
3.计算梯度Sobel/Scharr
4.非最大信号抑制
5.高低阈值输出二值图像
"""

import cv2 as cv

lena_img_path = '.\static\lena.png'


def edge_demo(image):
    # GaussianBlur消除噪声
    ima_blur = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(ima_blur, cv.COLOR_BGR2GRAY)
    # 计算梯度
    gradx = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    grady = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    # edge 二值边缘 两种都可以  50(低阈值), 150(高阈值) ，相差三倍
    # edge_output = cv.Canny(gradx, grady, 50, 150)
    edge_output = cv.Canny(gray, 50, 150)
    cv.imshow('edge_output', edge_output)

    # 彩色边缘
    dst = cv.bitwise_and(image, image, mask = edge_output)
    cv.imshow('edge_demo', dst)


def main():
    src = cv.imread(lena_img_path)
    cv.namedWindow('img', cv.WINDOW_AUTOSIZE)
    cv.imshow('img', src)

    begin_time = cv.getTickCount()

    edge_demo(src)

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time)/cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
