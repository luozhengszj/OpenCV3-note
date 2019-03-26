"""
图像膨胀和腐蚀
1.腐蚀
2.膨胀
彩色和灰度图像、单通道和多通道都支持

1.RGB色彩：红色R、绿色G、蓝色B三个通道
2.gray:
    任何颜色都有红、绿、蓝三原色组成，假如原来某点的颜色为RGB(R，G，B)，那么，我们可以通过下面几种方法，将其转换为灰度:
    1）浮点算法:Gray=R*0.3+G*0.59+B*0.11
    2）整数方法:Gray=(R*30+G*59+B*11)/100
    3）移位方法:Gray =(R*76+G*151+B*28)>>8;
    4）平均值法:Gray=(R+G+B)/3;
    5）仅取绿色:Gray=G;

    通过上述任一种方法求得Gray后，将原来的RGB(R,G,B)中的R,G,B统一用Gray替换，形成新的颜色RGB(Gray,Gray,Gray)，用它替换原来的RGB(R,G,B)就是灰度图了。
3.HSV色系：色调H，饱和度S，亮度V三个通道，详细如图

"""

import cv2 as cv

coins_img_path = r'.\static\8.jpg'


def erode_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    # 腐蚀块的大小(15, 15)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dst = cv.erode(binary, kernel)
    cv.imshow("erode_demo", dst)


def dilate_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    # 膨胀块的大小(5, 5)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.dilate(binary, kernel)
    cv.imshow("dilate_demo", dst)


def main():
    src = cv.imread(coins_img_path)
    cv.namedWindow('img', cv.WINDOW_AUTOSIZE)
    cv.imshow('img', src)

    begin_time = cv.getTickCount()

    # erode_demo(src)

    dilate_demo(src)

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time) / cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
