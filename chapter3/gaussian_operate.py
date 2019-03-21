"""
高斯模糊（比均值模糊去噪效果更好）
对高斯噪声效果较好。（椒盐是黑白）

"""

import numpy as np
import cv2 as cv


img_path = '.\static\example.png'


def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv


def gaussian_noise(image):
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)
            b = image[row, col, 0]  # blue
            g = image[row, col, 1]  # green
            r = image[row, col, 2]  # red
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.imshow("noise image", image)


def main():
    src = cv.imread(img_path)
    cv.namedWindow('img', cv.WINDOW_AUTOSIZE)
    cv.imshow('img', src)

    begin_time = cv.getTickCount()

    # gaussian_noise(src)

    # (0, 0)先起作用（由于0，所以无效，后面5就起效果了），5是模糊率
    dst = cv.GaussianBlur(src, (0, 0), 5)
    cv.imshow("Gaussian Blur", dst)

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time)/cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
