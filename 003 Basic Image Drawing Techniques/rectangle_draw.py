import cv2

# Draw rectangle on a image.png
image = cv2.imread('image.png')
top_left = (50, 50)  # Top-left corner of the rectangle
bottom_right = (200, 200)  # Bottom-right corner of the rectangle   
color = (0, 255, 0)  # Green color in BGR
thickness = 3  # Thickness of the rectangle border

cv2.rectangle(image, top_left, bottom_right, color, thickness)  # Draw the rectangle on the image
cv2.imwrite('image_with_rectangle.png', image)  # Save the modified image
cv2.imshow('Image with Rectangle', image)  # Display the image with the rectangle
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()   # Close all OpenCV window
