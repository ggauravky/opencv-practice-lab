import cv2

# Create a black image
image = cv2.imread('black_image.png')
center = (150, 150)  # Center of the circle
radius = 75  # Radius of the circle
color = (0, 0, 255)  # Red color in BGR
thickness = 4  # Thickness of the circle border
cv2.circle(image, center, radius, color, thickness)  # Draw the circle on the image
cv2.imwrite('image_with_circle.png', image)  # Save the modified image
cv2.imshow('Image with Circle', image)  # Display the image with the circle
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()   # Close all OpenCV windows