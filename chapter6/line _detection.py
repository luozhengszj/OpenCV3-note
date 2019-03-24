"""
直线检测:霍夫直线检测
步骤：
1.灰度图像cvtColor
2.边缘检测Canny
3.对边缘检测的结果进行霍夫直线检测
demo:
1.HoughLines（直接划出直线）
2.HoughLinesP（自定义参数划出线段）
"""

import cv2 as cv
import numpy as np

line_img_path = r'.\static\line.png'


def line_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    # threshold为边缘提取的低值，高值会会自己选择
    lines = cv.HoughLines(edges, 1, np.pi / 180, threshold=200)
    for line in lines:
        print(type(lines))
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv.imshow("image-lines", image)


def line_detect_possible_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    # minLineLength最小的那种线的长度，容忍的最大断线长度maxLineGap，threshold为边缘提取的低值，高值会会自己选择
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, threshold=150, minLineLength=50, maxLineGap=10)
    for line in lines:
        print(type(line))
        x1, y1, x2, y2 = line[0]
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv.imshow("line_detect_possible_demo", image)


def main():
    src = cv.imread(line_img_path)
    cv.namedWindow('img', cv.WINDOW_AUTOSIZE)
    cv.imshow('img', src)

    begin_time = cv.getTickCount()

    line_detection(src)

    line_detect_possible_demo(src)

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time) / cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
