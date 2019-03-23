"""
模板匹配
1.算法
2.应用场景：应用范围比较小，可能会受光线、噪声的影响
3.api
    多种匹配方法：TM_SQDIFF_NORMED、TM_CCORR_NORMED、TM_CCOEFF_NORMED

"""

import numpy as np
import cv2 as cv

c_img_path = '.\static\c.png'
ctemplate_img_path = '.\static\c_template.png'


def template_demo():
    c = cv.imread(c_img_path)
    c_template = cv.imread(ctemplate_img_path)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw = c_template.shape[:2]

    for md in methods:
        print(md)
        result = cv.matchTemplate(c, c_template, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        # 匹配的地方圈起来
        br = (tl[0] + tw, tl[1] + th)
        cv.rectangle(c, tl, br, (0, 0, 255), 2)
        cv.imshow('match'+np.str(md),c)
        # cv.imshow('match' + np.str(md), result)


def main():
    """
    src = cv.imread(c_img_path)
    cv.namedWindow('c img', cv.WINDOW_AUTOSIZE)
    cv.imshow('c img', src)
    """

    begin_time = cv.getTickCount()

    template_demo()

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time)/cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
