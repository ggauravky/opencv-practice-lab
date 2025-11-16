import cv2
import numpy as np

# Load the image
image = cv2.imread('C:\\Users\\Lenovo\\VS Code Files\\Python\\OpenCV\\005 Image Filtering & Blurring\\h\\image.png')
# Apply sharpening filter
sharpening_kernel = np.array([[0, -1, 0],
                                [-1, 5,-1],
                                [0, -1, 0]])
sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)
# Save the sharpened image
cv2.imwrite('sharpened_image.jpg', sharpened_image)
# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()