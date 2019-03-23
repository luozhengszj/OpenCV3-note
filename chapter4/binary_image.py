"""
图像二值化
一、好的图像图像二值化（如图中分像素点）
二、二值化的方法：
1.OTSU
2.Triangle：对图像的直方图单波峰效果更好，多个不好
3.局部域值：对局部图像线条二值化更好
4.自定义域值

三、超大图像二值化（几M甚至更大）
1.分块
2.全局域值 局部域值

"""

import numpy as np
import cv2 as cv

text_img_path = r'.\static\text.png'
c_img_path = '.\static\c.png'


def threshold_demo(image):
    # 首先灰度图像
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # 后面有cv.THRESH_OTSU，所以0不发生作用    cv.THRESH_BINARY | cv.THRESH_OTSU | cv.THRESH_TRIANGLE
    # ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # threshold value 109.0
    # 109发生作用
    ret, binary = cv.threshold(gray, 109, 255, cv.THRESH_BINARY)
    # ret, binary = cv.threshold(gray, 109, 255, cv.THRESH_BINARY_INV)  # 和上一个颜色相反
    # ret, binary = cv.threshold(gray, 109, 255, cv.THRESH_TRUNC)  # 颜色截断
    print('threshold value %s'%ret)
    cv.imshow('binary', binary)


# 局部域值
def local_threshold_demo(image):
    # 首先灰度图像
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # 10去掉噪声影响
    # binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 10)
    # 相对来说，ADAPTIVE_THRESH_GAUSSIAN_C更好
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow('binary', binary)



# 自己计算均值，从而自定义二值化
def custom_threshold_demo(image):
    # 首先灰度图像
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w * h])
    mean = m.sum() / (w * h)
    print("mean : ", mean)
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    cv.imshow("binary", binary)


# 超大图像二值化
def big_image_binary(image):
    print(image.shape)
    #大图像的时候一般是这样设置（cw = 256，ch = 256），由于选择的是小图像，所以用的（cw = 60，ch = 60）
    """
    cw = 256
    ch = 256
    """
    cw = 60
    ch = 60  #图像太小，分割的块太小，效果不好，但是能看清楚原理
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row+ch, col:col+cw]
            # ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 全局域值
            # 局部自定义域值（效果比较好）
            # dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 20)
            # 127未基数，10块的大小（去噪声）
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 10)
            gray[row:row + ch, col:col + cw] = dst
            print(np.std(dst), np.mean(dst))
            print(np.std(roi), np.mean(roi))

    cv.imshow('gray', gray)


# 超大图像二值化（优化全局域值：加上空白图像的处理）
def big_image_binary_optimization(image):
    print(image.shape)
    #大图像的时候一般是这样设置（cw = 256，ch = 256），由于选择的是小图像，所以用的（cw = 60，ch = 60）
    """
    cw = 256
    ch = 256
    """
    cw = 60
    ch = 60  #图像太小，分割的块太小，效果不好，但是能看清楚原理
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row + ch, col:cw + col]
            print(np.std(roi), np.mean(roi))
            dev = np.std(roi)
            if dev < 5:
                gray[row:row + ch, col:cw + col] = 255
            else:
                ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
                gray[row:row + ch, col:cw + col] = dst

    cv.imshow('gray', gray)


def main():

    src = cv.imread(c_img_path)
    cv.namedWindow('c img', cv.WINDOW_AUTOSIZE)
    cv.imshow('c img', src)

    begin_time = cv.getTickCount()

    # threshold_demo(src)

    # local_threshold_demo(src)

    # custom_threshold_demo(src)

    text_img_src = cv.imread(text_img_path)
    # big_image_binary(text_img_src)
    big_image_binary_optimization(text_img_src)

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time)/cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
