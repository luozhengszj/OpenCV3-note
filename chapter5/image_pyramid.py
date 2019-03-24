"""
图像金字塔  lena像素必须为2的n次方
1.reduce 降采样
2.expand 扩大
"""

import cv2 as cv

lena_img_path = r'.\static\lena.png'


def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow("pyramid_down_"+str(i), dst)
        temp = dst.copy()
    return pyramid_images


def lapalian_demo(image):
    pyramid_images = pyramid_demo(image)
    lens = len(pyramid_images)
    for i in range(lens - 1, -1 , -1):
        # 最后一层的特殊处理
        if (i - 1) < 0:
            expand = cv.pyrUp(pyramid_images[i], dstsize=image.shape[:2])
            lpls = cv.subtract(image, expand)
            cv.imshow("lapalian_down_" + str(i), lpls)
        else:
            expand = cv.pyrUp(pyramid_images[i], dstsize=pyramid_images[i - 1].shape[:2])
            lpls = cv.subtract(pyramid_images[i - 1], expand)
            cv.imshow("lapalian_down_" + str(i), lpls)


def main():

    src = cv.imread(lena_img_path)
    cv.namedWindow('lena img', cv.WINDOW_AUTOSIZE)
    cv.imshow('lena img', src)

    begin_time = cv.getTickCount()

    # pyramid_demo(src)

    lapalian_demo(src)

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time)/cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()