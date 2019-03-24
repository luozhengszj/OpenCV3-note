"""
轮廓发现
1.去噪
2.灰度图像
3.二值图像
4.findContours发现轮廓
5.drawContours描绘轮廓
6.计算出轮廓，就可以进行轮廓的分析，如面积周长等

"""

import cv2 as cv

line_img_path = r'.\static\coins.jpg'


def contours_demo(image):
    # 高斯模糊去噪
    dst = cv.GaussianBlur(image, (3, 3), 0)
    # 灰度图像
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    # 图像二值化
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary image", binary)
    # 发现轮廓（树形RETR_TREE、RETR_EXTERNAL）
    contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        # 整个轮廓描绘红色
        cv.drawContours(image, contours, i, (0, 0, 255), -1)
        print(i)
    cv.imshow("detect contours", image)


def contours_edge_demo(image):
    binary = edge_demo(image)

    contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), -1)
        approxCurve = cv.approxPolyDP(contour, 4, True)
        if approxCurve.shape[0] > 6:
            cv.drawContours(image, contours, i, (0, 0, 255), 2)
        if approxCurve.shape[0] == 4:
            cv.drawContours(image, contours, i, (255, 255, 0), 2)
        print(approxCurve.shape[0])
        print(i)
    cv.imshow("detect contours", image)


# 边缘提取方法
def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    # X Gradient
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    # Y Gradient
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    # edge
    edge_output = cv.Canny(xgrad, ygrad, 50, 150)  # 硬币时候的高低阈值
    # edge_output = cv.Canny(gray, 30, 100)  # 多形状图片的高低阈值
    cv.imshow("Canny Edge", edge_output)
    return edge_output


def main():
    src = cv.imread(line_img_path)
    cv.namedWindow('img', cv.WINDOW_AUTOSIZE)
    cv.imshow('img', src)

    begin_time = cv.getTickCount()

    # contours_demo(src)

    contours_edge_demo(src)

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time) / cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
