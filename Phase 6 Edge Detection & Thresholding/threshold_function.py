import cv2

# Thresholding function
def apply_threshold(image_path, threshold_value):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply binary thresholding
    _, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    
    return thresholded_image
# Example usage
if __name__ == "__main__":
    image_path = 'Phase 6 Edge Detection & Thresholding\\img.jpg'
    threshold_value = 128
    
    thresholded_image = apply_threshold(image_path, threshold_value)
    
    # Save the thresholded image
    cv2.imwrite('thresholded_image.jpg', thresholded_image)
    
    # Display the thresholded image
    cv2.imshow('Thresholded Image', thresholded_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()