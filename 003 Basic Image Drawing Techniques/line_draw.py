import cv2

#draw a line on a image.png
image = cv2.imread('image.png')
start_point = (50, 50)  # Starting point of the line
end_point = (200, 200)  # Ending point of the line
color = (255, 0, 0)  # Blue color in BGR
thickness = 5  # Thickness of the line
cv2.line(image, start_point, end_point, color, thickness)  # Draw the line on the image
cv2.imwrite('image_with_line.png', image)  # Save the modified image
cv2.imshow('Image with Line', image)  # Display the image with the line
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()   # Close all OpenCV windows