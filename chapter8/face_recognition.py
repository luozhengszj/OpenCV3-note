"""
基于级联检测器的人脸识别
需要光线较强的情况下才能比较准确

"""

import cv2 as cv

timg_img_path = r'.\static\timg.jpg'
frontalface_path = r'.\static\haarcascade_frontalface_alt_tree.xml'


def face_detect_demo(image):
    # 基于灰度图像进行的人脸检测
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # 通过级联检测器加载特征数据
    face_detector = cv.CascadeClassifier(frontalface_path)
    # 第三个参数，越高表示检测要求越严格，一般为 2，3，5比较合适，第二个参数表示金字塔层数
    faces = face_detector.detectMultiScale(gray, 1.1, 2)
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 1)
    cv.imshow("result", image)


# 摄像头的人脸跟踪
def capture_face_detect_demo():
    capture = cv.VideoCapture(0)
    cv.namedWindow("result", cv.WINDOW_AUTOSIZE)
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        face_detect_demo(frame)
        c = cv.waitKey(10)
        if c == 27:  # ESC
            break


def main():
    src = cv.imread(timg_img_path)

    begin_time = cv.getTickCount()

    # face_detect_demo(src)

    capture_face_detect_demo()

    end_time = cv.getTickCount()
    print('run time (s): %s' % ((end_time - begin_time) / cv.getTickFrequency()))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
