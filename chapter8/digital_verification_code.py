"""
基于OpenCV+Tesserct-OCR的数字验证码识别
1.OpenCV预处理
2.Tesserct-OCR验证码识别
需要先安装Tesserct-OCR，具体可参照博客
https://www.cnblogs.com/jianqingwang/p/6978724.html

"""

import cv2 as cv
import numpy as np
from PIL import Image
import pytesseract as tess

vercode_img_path = r'.\static\vercode.png'


def recognize_text(src):
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 2))
    bin1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 1))
    open_out = cv.morphologyEx(bin1, cv.MORPH_OPEN, kernel)
    cv.imshow("binary-image", open_out)

    cv.bitwise_not(open_out, open_out)
    textImage = Image.fromarray(open_out)
    text = tess.image_to_string(textImage)
    print("识别结果: %s" % text)


def main():
    src = cv.imread(vercode_img_path)

    begin_time = cv.getTickCount()

    recognize_text(src)

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time) / cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()

"""
课程结束~~~
"""
