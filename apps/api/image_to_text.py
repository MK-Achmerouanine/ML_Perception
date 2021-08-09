import cv2
import numpy as np
import pytesseract


def preprocess(img_path):

    # This function performs preprocessing operations such as gray scaling,
    # thresholding and rotating the image if
    # text is not aligned as well as surrounding text.

    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh1 = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
    cords = np.column_stack(np.where(thresh1 == 0))
    angle = cv2.minAreaRect(cords)[-1]

    if angle < -45:
        angle = -(90 + angle)

    elif angle > 45:
        angle = -angle + 90
        if 50 > angle > 40:
            angle = angle
    else:
        angle = -angle

    # if angle < -45:
    #     angle = 90 + angle
    # angle = -1.0 * angle

    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = img.copy()
    cv2.warpAffine(img, rotation_matrix, (w, h), rotated,
                   cv2.INTER_CUBIC, cv2.BORDER_REPLICATE)
    gray = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)
    thresh1 = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
    # rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    # dilation = cv2.dilate(thresh1, rect_kernel, iterations=4)
    # cv2.imshow("Text", dilation)
    # cv2.waitKey(0)
    return thresh1


def image_to_text():
    thresh = preprocess()
    text = pytesseract.image_to_string(thresh, lang='eng')
    text_file = open('Out.txt', 'w')
    text_file.write(text)
    text_file.close()
    return text
