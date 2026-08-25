import cv2
image = cv2.imread("iris-1.jpg")

def print_image_information(image):
    print(f"Height: {image.shape[0]}")
    print(f"Width : {image.shape[1]}")
    print(f"Channel : {image.shape[2]}")
    print(f"Size :{image.size}")
    print(f"Data type : {image.dtype}")

print_image_information(image)

