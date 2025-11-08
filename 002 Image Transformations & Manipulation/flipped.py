import cv2

# image = cv2.imread("image.png")
image = cv2.imread("C:\\Users\\Lenovo\\VS Code Files\\Python\\OpenCV\\002 Image Transformations & Manipulation\\image.png")

if image is None:
    print("Could not read the image.")
else:
    flipped_image = cv2.flip(image, 1)  # Flip the image horizontally
    flipped_image_vertical = cv2.flip(image, 0)  # Flip the image vertically
    flipped_image_both = cv2.flip(image, -1)  # Flip the image both horizontally and vertically
    
    cv2.imshow("Original Image", image) # Display the original image
    cv2.imshow("Flipped Image (Horizontal)", flipped_image) # Display the horizontally flipped image
    cv2.imshow("Flipped Image (Vertical)", flipped_image_vertical) # Display the vertically flipped image
    cv2.imshow("Flipped Image (Both)", flipped_image_both)  # Display the image flipped both ways
    

    cv2.waitKey(0)
    cv2.destroyAllWindows() 