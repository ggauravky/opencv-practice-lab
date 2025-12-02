import cv2

#canny edge detection function
def canny_edge_detection(image_path, low_threshold, high_threshold):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply Canny edge detection
    edges = cv2.Canny(image, low_threshold, high_threshold)
    
    return edges

# Example usage
if __name__ == "__main__":
    image_path = 'Phase 6 Edge Detection & Thresholding\\img.jpg'
    low_threshold = 100
    high_threshold = 200
    
    edges = canny_edge_detection(image_path, low_threshold, high_threshold)
    
    # Save the edges image
    cv2.imwrite('canny_edges.jpg', edges)
    
    # Display the edges image
    cv2.imshow('Canny Edges', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()