import cv2

# image = cv2.imread("image.png")
image = cv2.imread("C:\\Users\\Lenovo\\VS Code Files\\Python\\OpenCV\\002 Image Transformations & Manipulation\\image.png")
if image is not None:
    print("Image Loaded successfully")
    
    cropped_image = image[50:300, 100:400]
    # Cropping the image: rows 50 to 300 and columns 100 to 400
    # Format: image[y1:y2, x1:x2]

    cv2.imshow('original', image)
    cv2.imshow('cropped', cropped_image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()