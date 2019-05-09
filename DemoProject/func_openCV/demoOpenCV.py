import os
from common.logger import get_logger
import cv2

logger = get_logger(os.path.splitext(os.path.basename(__file__))[0])

CLASSIFIERS_FACE = "C:\\DevTools\\ProjectTools\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
CLASSIFIERS_EYE = "C:\\DevTools\\ProjectTools\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml"
IMG_NAME = ".\\resources\\Lenna_(test_image).png"


def demo():
    logger.info("Demo START")

    img_color = cv2.imread(IMG_NAME, cv2.IMREAD_COLOR)
    img_gray = cv2.imread(IMG_NAME, cv2.IMREAD_GRAYSCALE)

    cv2.imshow("DemoPhoto1", img_color)
    cv2.imshow("DemoPhoto2", img_gray)

    cv2.waitKey()
    cv2.destroyAllWindows()

    logger.info("Demo END")


def demo2():
    logger.info("Demo START")

    face_cascade = cv2.CascadeClassifier(CLASSIFIERS_FACE)
    eye_cascade = cv2.CascadeClassifier(CLASSIFIERS_EYE)

    img_color = cv2.imread(IMG_NAME, cv2.IMREAD_COLOR)
    img_gray = cv2.imread(IMG_NAME, cv2.IMREAD_GRAYSCALE)

    faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img_color = cv2.rectangle(img_color, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = img_gray[y:y + h, x:x + w]
        roi_color = img_color[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('DemoPhoto', img_color)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    logger.info("Demo END")
