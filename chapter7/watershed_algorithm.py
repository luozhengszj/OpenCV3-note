"""
分水岭算法  运用于图像分割
基于距离变换的分水岭算法流程

"""

import numpy as np
import cv2 as cv

coins_img_path = r'.\static\coins.jpg'


def watershed_demo(src):
    # remove noise if any
    print(src.shape)
    blurred = cv.pyrMeanShiftFiltering(src, 10, 100)
    # gray\binary image
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary-image", binary)

    # morphology operation
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv.dilate(mb, kernel, iterations=3)
    cv.imshow("mor-opt", sure_bg)

    # distance transform
    dist = cv.distanceTransform(mb, cv.DIST_L2, 3)
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    # cv.imshow("distance-t", dist_output * 50)  # 4.0出错(-215:Assertion failed) dst.data == (uchar*)dst_ptr in function 'cvShowImage'

    ret, surface = cv.threshold(dist, dist.max() * 0.6, 255, cv.THRESH_BINARY)

    surface_fg = np.uint8(surface)
    cv.imshow("surface-bin", surface_fg)
    unknown = cv.subtract(sure_bg, surface_fg)
    ret, markers = cv.connectedComponents(surface_fg)

    # watershed transform
    markers = markers + 1
    markers[unknown == 255] = 0
    markers = cv.watershed(src, markers=markers)
    src[markers == -1] = [0, 0, 255]
    cv.imshow("result", src)


def main():
    src = cv.imread(coins_img_path)

    begin_time = cv.getTickCount()

    watershed_demo(src)

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time) / cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
