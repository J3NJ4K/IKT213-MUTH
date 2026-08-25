import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("iris-1.png")
lena = cv2.imread("lena.png")
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
    cv2.imwrite("padding_result.png", replicate)

    plt.imshow(cv2.cvtColor(replicate, cv2.COLOR_BGR2RGB))
    plt.title("Image with reflect border")
    plt.axis('off')
    plt.show()
    return replicate

padding(img, 100)

def crop(image, x_0, x_1, y_0, y_1):
    cropped_img = image[y_0:y_1, x_0:x_1]
    cv2.imwrite("cropped_image.png",cropped_img)

    plt.imshow(cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB))
    plt.title("Cropped image")
    plt.axis("off")
    plt.show()
    return cropped_img

crop(img, 200, 670, 200, 470)

def resize(image, width, height):
    resized_image = cv2.resize(image, (width, height))
    cv2.imwrite("resized_image.png", resized_image)

    plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
    plt.title("Resized image")
    plt.axis("off")
    plt.show()
    return resized_image

resize(img, 200,200)

def copy(image, emptyPictureArray):
    height, width, channels = image.shape
    for y in range(height):
        for x in range(width):
            emptyPictureArray[y, x] = image[y, x]
    cv2.imwrite("copy.png", emptyPictureArray)

    plt.imshow(cv2.cvtColor(emptyPictureArray, cv2.COLOR_BGR2RGB))
    plt.title("Image copy")
    plt.axis("off")
    plt.show()
    return emptyPictureArray

height, width, channels = lena.shape
empty_array = np.zeros((height,width,3), dtype=np.uint8)
copy(lena, empty_array)

def grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gray.png", gray)

    plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
    plt.title("Gray image")
    plt.axis("off")
    plt.show()
    return gray

grayscale(img)

def hsv(image):
    hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imwrite("hsv.png", hsvImage)

    plt.imshow(cv2.cvtColor(hsvImage, cv2.COLOR_BGR2RGB))
    plt.title("HSV image")
    plt.axis("off")
    plt.show()
    return hsvImage

hsv(img)

def hue_shifted(image, emptyPictureArray, hue):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv_image)
    h_new = np.mod(h.astype(int) + hue, 180).astype(np.uint8)
    hsv_new = cv2.merge([h_new,s,v])
    bgr_new = cv2.cvtColor(hsv_new, cv2.COLOR_HSV2BGR)
    emptyPictureArray[:] = bgr_new[:]
    cv2.imwrite("hue_shifted.png",emptyPictureArray)
    return emptyPictureArray

h, w, c = img.shape
empty_array = np.zeros((h, w, c), dtype=np.uint8)

shifted_result = hue_shifted(img, empty_array, 50)

plt.imshow(cv2.cvtColor(shifted_result, cv2.COLOR_BGR2RGB))
plt.title("Shifed image (+50)")
plt.axis("off")
plt.show()

def smoothing(image):
    blurred_with_border = cv2.GaussianBlur(image,(15,15), sigmaX=0, borderType=cv2.BORDER_DEFAULT)
    cv2.imwrite("smoothed.png", blurred_with_border)
    return blurred_with_border

smooth_image = smoothing(img)
plt.imshow(cv2.cvtColor(smooth_image, cv2.COLOR_BGR2RGB))
plt.title("Smoothed image")
plt.axis("off")
plt.show()

def rotation(image, rotation_angle):
    if rotation_angle == 90:
        rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif rotation_angle == 180:
        rotated = cv2.rotate(image, cv2.ROTATE_180)
    cv2.imwrite("rotated.png", rotated)
    return rotated

rotated_90 = rotation(img,90)
plt.imshow(cv2.cvtColor(rotated_90, cv2.COLOR_BGR2RGB))
plt.title("Rotated 90")
plt.axis("off")
plt.show()

rotated_180 = rotation(img, 180)
plt.imshow(cv2.cvtColor(rotated_180, cv2.COLOR_BGR2RGB))
plt.title("Rotated 180")
plt.axis("off")
plt.show()
