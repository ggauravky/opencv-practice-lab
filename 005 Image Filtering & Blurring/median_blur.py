import cv2

# Load the image
image = cv2.imread('input_image.jpg')
# Apply median blur
median_blurred_image = cv2.medianBlur(image, 15)
# Save the median blurred image
cv2.imwrite('median_blurred_image.jpg', median_blurred_image)
# Display the original and median blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Median Blurred Image', median_blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
