import cv2
import numpy as np
import sys

lambo = cv2.imread("lambo.png")
shapes = cv2.imread("shapes-1.png")
shapes_template = cv2.imread("shapes_template.jpg")

def sobel_edge_detection(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_blur = cv2.GaussianBlur(image_gray, (3, 3), 0)
    sobel = cv2.Sobel(src = image_blur, ddepth = cv2.CV_32F, dx = 1, dy = 1, ksize = 1)
    sobel_8u = np.clip(sobel * 255, 0, 255).astype(np.uint8)
    cv2.imwrite("sobel_8u.png", sobel_8u)
    return sobel

cv2.imshow("sobel edge detection", sobel_edge_detection(lambo))
cv2.waitKey(0)

def canny_edge_detection(image, threshold1, threshold2):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)
    edges = cv2.Canny(img_blur, threshold1, threshold2)
    cv2.imwrite("canny_edge.png", edges)
    return edges

cv2.imshow("canny_edge_detection", canny_edge_detection(lambo, 50, 50))
cv2.waitKey(0)

def template_match(image, template):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    temp = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = temp.shape[::-1]

    res = cv2.matchTemplate(img_gray, temp, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    cv2.imwrite("template_match.png",image)
    return image

cv2.imshow("template_match", template_match(shapes, shapes_template))
cv2.waitKey(0)
cv2.destroyAllWindows()

def resize(image, scale_factor:int, up_or_down:str):
    rows, cols,  _channels = map(int, image.shape)

    if up_or_down == "up":
        resized_image = cv2.pyrUp(image, dstsize = (scale_factor*cols, scale_factor*rows))
    elif up_or_down == "down":
        resized_image = cv2.pyrDown(image, dstsize = (cols//scale_factor, rows//scale_factor))
    else:
        print("Invalid up or down input")
        return image

    cv2.imwrite("resized_image.png", resized_image)
    return resized_image

direction = input("Type in direction 'up' or 'down' :")

resized_image = resize(lambo, scale_factor=2, up_or_down=direction)
cv2.imshow("resized image", resized_image)
cv2.waitKey(0)


