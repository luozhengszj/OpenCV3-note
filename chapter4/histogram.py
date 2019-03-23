"""
图像的直方图
1.直方图的含义
2.直方图的应用（自动调整对比度、增强图像的手段）:两种方法
3.直方图的均衡化
4.直方图的比较：图片大小一致，不一致需要先规划再比较（巴氏距离、直方图相关性、卡方）
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


rise_img_path = r'.\static\rice.png'
hist_compare_path1 = r'.\static\lena.png'
hist_compare_path2 = r'.\static\lenanoise.png'


def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show('直方图')


def image_hist(image):
    color = ['blue', 'green', 'red']
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])

        plt.plot(hist, color = color)
        plt.xlim([0, 256])
    plt.show('image_hist')


# 图像增强（参数不可设置）
def equalHist_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow('equalHist_demo', dst)


# 这种可以对增强效果进行干涉，上面的不可以
def clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # clipLimit增强的强度（默认40），tileGridSize块的大小
    clahe = cv.createCLAHE(clipLimit=5.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow('clahe_demo', dst)


def create_hist_demo(image):
    h, w, c = image.shape
    rgbHist = np.zeros([16*16*16, 1], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b/bsize)*16*16 + np.int(g/bsize)*16 + np.int(r/bsize)
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1
    return rgbHist


# 图片比较： 图片大小不一样的时候需要规划之后才能比较
def hist_compare(image1, image2):
    hist1 = create_hist_demo(image1)
    hist2 = create_hist_demo(image2)
    # 巴式距离 大则不相似，最大1
    match1 =cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    # 直方图相关性  很小很不相似，1则是一样
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    # 卡方比较 大增相差大
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)

    print('巴式距离：%s，直方图相关性：%s，卡方比较：%s'%(match1, match2, match3))


def main():
    src = cv.imread(rise_img_path)
    cv.imshow('rise_img', src)

    src1 = cv.imread(hist_compare_path1)
    src2 = cv.imread(hist_compare_path2)
    cv.imshow('rise_img', src)
    cv.imshow('lena1', src1)
    cv.imshow('lena', src2)
    begin_time = cv.getTickCount()

    # plot_demo(src)
    # image_hist(src)

    # equalHist_demo(src)
    # clahe_demo(src)

    hist_compare(src, src1)
    hist_compare(src1, src2)
    """
    巴式距离：0.9483004783902151，直方图相关性：0.07983002590487684，卡方比较：326868.954847833
    巴式距离：0.09072200336618969，直方图相关性：0.9788106004024394，卡方比较：164.3082768373199
    run time (s): 13.76500677002822
    """

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time)/cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
