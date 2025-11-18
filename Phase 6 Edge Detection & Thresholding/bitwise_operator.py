import numpy as np
import cv2

# Bitwise AND operation function
def bitwise_and_operation(image_path1, image_path2):
    # Load the images
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)
    
    # Ensure both images are of the same size
    if image1.shape != image2.shape:
        raise ValueError("Images must be of the same size for bitwise AND operation.")
    
    # Apply bitwise AND operation
    bitwise_and_result = cv2.bitwise_and(image1, image2)
    
    return bitwise_and_result

#Bitwise OR operation function
def bitwise_or_operation(image_path1, image_path2):
    # Load the images
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)
    
    # Ensure both images are of the same size
    if image1.shape != image2.shape:
        raise ValueError("Images must be of the same size for bitwise OR operation.")
    
    # Apply bitwise OR operation
    bitwise_or_result = cv2.bitwise_or(image1, image2)
    
    return bitwise_or_result

#Bitwise NOT operation function
def bitwise_not_operation(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Apply bitwise NOT operation
    bitwise_not_result = cv2.bitwise_not(image)
    
    return bitwise_not_result

# Example usage
if __name__ == "__main__":
    image_path1 = 'Phase 6 Edge Detection & Thresholding\\img.jpg'
    image_path2 = 'Phase 6 Edge Detection & Thresholding\\img2.jpg'
    
    and_result = bitwise_and_operation(image_path1, image_path2)
    or_result = bitwise_or_operation(image_path1, image_path2)
    not_result = bitwise_not_operation(image_path1)
    
    # Save the results
    cv2.imwrite('bitwise_and_result.jpg', and_result)
    cv2.imwrite('bitwise_or_result.jpg', or_result)
    cv2.imwrite('bitwise_not_result.jpg', not_result)
    
    # Display the results
    cv2.imshow('Bitwise AND Result', and_result)
    cv2.imshow('Bitwise OR Result', or_result)
    cv2.imshow('Bitwise NOT Result', not_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()