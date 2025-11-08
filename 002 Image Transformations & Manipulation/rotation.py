import cv2

# image = cv2.imread("image.png")
image = cv2.imread("C:\\Users\\Lenovo\\VS Code Files\\Python\\OpenCV\\002 Image Transformations & Manipulation\\image.png")

if image is None:
    print("Could not read the image.")
else:
    (h,w)= image.shape[:2]
    center = (w//2, h//2)
    matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated = cv2.warpAffine(image, matrix, (w,h))

    cv2.imshow('original', image)
    cv2.imshow('rotated', rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()