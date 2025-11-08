import cv2

# image = cv2.imread("image.png")
image = cv2.imread("C:\\Users\\Lenovo\\VS Code Files\\Python\\OpenCV\\002 Image Transformations & Manipulation\\image.png")

if image is None:
    print("Error loading image")
else:
    print("Image Loaded successfully")
    
    resized_image = cv2.resize(image, (400, 400))

    cv2.imshow('original', image)
    cv2.imshow('resized', resized_image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()