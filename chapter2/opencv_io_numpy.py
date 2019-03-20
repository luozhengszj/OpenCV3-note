"""
图像处理操作：
1.获取图像信息（通道、大小等）
2.图像倒置（利用循环、利用numpy）
3.摄像头操作，同样可以运用于视频
"""

import numpy as np
import cv2 as cv

img_path = '.\static\cat.png'


# 获取图像具体信息
def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)  # size = 三通道相乘 蓝绿红 blue,gre
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


# numpy
def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print('width: %s, height: %s, channels: %s'%(width, height, channels))
    """
    # 利用numpy倒置图片
    dst = cv.bitwise_not(image)
    cv.imshow('pixels image', dst)
    """
    # 循环倒置图片 慢！
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv

    cv.imshow('pixels image', image)


# 利用numpy创建图片
def create_image():
    """
    img = np.zeros([400, 400, 3], np.uint8)
    img[:, :, 1] = np.ones([400, 400]) * 255
    """

    """
    img = np.zeros([400, 400, 1], np.uint8)
    img[:, :, 0] = np.ones([400, 400]) * 127
    """

    """
    img = np.ones([400, 400, 1], np.uint8)
    img = img * 127  # 和上面效果一样
    """

    # cv.imshow('create image', img)

    # img = np.ones([3, 3], np.float32)  # 类型影响截断！！会影响大小
    img = np.ones([3, 3], np.uint8)
    img.fill(12227.8888)

    img2 = img.reshape([1, 9])
    print(img)
    print(img2)


# 获取摄像头视频
def video_demo():
    capture = cv.VideoCapture(0)  # 写入视频路径或第几个摄像头
    while 1:
        ret, frame = capture.read()
        cv.flip(frame, 1)  # 把视频取正
        cv.imshow('video', frame)
        c = cv.waitKey(50)
        if c == 27:
            break


def main():
    src = cv.imread(img_path)
    cv.namedWindow('cat img', cv.WINDOW_AUTOSIZE)
    cv.imshow('cat img', src)

    # get_image_info(src)
    # gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY) #灰度图像
    # cv.imwrite('.\static\cat_copy.png', gray) #保存图像
    # video_demo() #读取摄像头视频

    begin_time = cv.getTickCount()

    access_pixels(src)
    # create_image()

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time)/cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
