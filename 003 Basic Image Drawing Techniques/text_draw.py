import cv2

# Create a black image
image = cv2.imread('image.png')
text = 'Hello, OpenCV!'  # Text to be drawn
position = (50, 150)  # Bottom-left corner of the text  
font = cv2.FONT_HERSHEY_SIMPLEX  # Font type
font_scale = 1  # Font scale
color = (255, 255, 255)  # White color in BGR
thickness = 2  # Thickness of the text
cv2.putText(image, text, position, font, font_scale, color, thickness)  # Draw the text on the image
cv2.imwrite('image_with_text.png', image)  # Save the modified image
cv2.imshow('Image with Text', image)  # Display the image with the text
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows