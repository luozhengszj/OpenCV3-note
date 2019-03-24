"""
圆检测:霍夫园检测（对噪声敏感，所以需要去噪）
如果不进行均值迁徙去噪，结果误差极大

"""

import cv2 as cv
import numpy as np

line_img_path = r'.\static\coins.jpg'


def detect_circles_demo(image):
    # 均值迁徙
    dst = cv.pyrMeanShiftFiltering(image, 10, 100)
    # 变为灰度图像
    cimage = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    """
    霍夫圆检测：
    image，选择的方法（HOUGH_GRADIENT基于梯度），minDist（圆心距离超过这个值则是不同心圆，反之同心圆），
    circles:同个圆，param1，minRadius圆最小距离，maxRadius圆最大距离
    """
    circles = cv.HoughCircles(cimage, method=cv.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)
    # 转整
    circles = np.uint16(np.around(circles))
    # 对园进行画圈
    for i in circles[0, :]:
        """
        center圆心，thickness线宽，color线颜色
        """
        cv.circle(image, center=(i[0], i[1]), radius=i[2], color=(0, 0, 255), thickness=2)
        cv.circle(image, (i[0], i[1]), 2, (255, 0, 0), 2)
    cv.imshow("circles", image)


def main():
    src = cv.imread(line_img_path)
    cv.namedWindow('img', cv.WINDOW_AUTOSIZE)
    cv.imshow('img', src)

    begin_time = cv.getTickCount()

    detect_circles_demo(src)

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time) / cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
