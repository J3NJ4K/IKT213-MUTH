import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("iris-1.png")

#image dimension to use later for crop function
print(img.shape)

def padding(image, border_width):
    replicate = cv2.copyMakeBorder(
        image,
        top=border_width,
        bottom=border_width,
        left=border_width,
        right=border_width,
        borderType=cv2.BORDER_REFLECT
    )
    cv2.imwrite("padding.png", replicate)
    return replicate

def crop(image, x_0, x_1, y_0, y_1):
    cropped = image[y_0:y_1, x_0:x_1]
    cv2.imwrite("cropped.png", cropped)
    return cropped

def resize(image, width, height):
    resized = cv2.resize(image, (width, height))
    cv2.imwrite("resized.png", resized)
    return resized

def copy(image, emptyPictureArray):
    height, width, channels = image.shape
    for y in range(height):
        for x in range(width):
            emptyPictureArray[y, x] = image[y, x]
    cv2.imwrite("copy.png", emptyPictureArray)
    return emptyPictureArray

def grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gray.png", gray)
    return gray

def hsv(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imwrite("hsv.png",hsv)
    return hsv

def hue_shifted(image, emptyPictureArray, hue):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    h_new = np.mod(h.astype(int) + hue, 180).astype(np.uint8)
    hsv_new = cv2.merge([h_new, s, v])
    bgr_new = cv2.cvtColor(hsv_new, cv2.COLOR_HSV2BGR)
    emptyPictureArray[:] = bgr_new[:]
    cv2.imwrite("hue_shifted.png", emptyPictureArray)
    return emptyPictureArray

def smoothing(image):
    blurred_with_border = cv2.GaussianBlur(image, (15,15), sigmaX=0, borderType=cv2.BORDER_DEFAULT)
    cv2.imwrite("smoothed.png",blurred_with_border)
    return blurred_with_border

def rotation(image, rotation_angle):
    if rotation_angle == 90:
        rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif rotation_angle == 180:
        rotated = cv2.rotate(image, cv2.ROTATE_180)
    cv2.imwrite("rotated.png", rotated)
    return rotated

def show_image(title, image):
    plt.figure()
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")

pad_img = padding(img, 100)
show_image("Padding", pad_img)

crop_img = crop(img, 200, 670, 200, 470)
show_image("Cropped", crop_img)

resized_img = resize(img, 200, 200)
show_image("Resized", resized_img)

height, width, channels = img.shape
empty_array = np.zeros((height, width, 3), dtype=np.uint8)
copied_img = copy(img, empty_array)
show_image("Copied image", copied_img)

gray_img = grayscale(img)
show_image("Gray image", gray_img)

hsv_img = hsv(img)
show_image("HSV", hsv_img)

empty_array = np.zeros((height, width, channels), dtype=np.uint8)
shifted_img = hue_shifted(img, empty_array, 50)
show_image("Shifted image", shifted_img)

smooth_img = smoothing(img)
show_image("Smoothed", smooth_img)

rot90 = rotation(img, 90)
show_image("Rotated 90", rot90)

rot180 = rotation(img, 180)
show_image("Rotated 180", rot180)

plt.show()