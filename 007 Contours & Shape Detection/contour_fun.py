import cv2

img = cv2.imread("C:\\Users\\Lenovo\\VS Code Files\\Python\\OpenCV\\007 Contours & Shape Detection\\circle.png")
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply edge detection using Canny
edges = cv2.Canny(gray, 50, 150)

# Find contours
contours, hierarchy = cv2.findContours(
    edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)  # RETR_EXTERNAL retrieves only the external contours, CHAIN_APPROX_SIMPLE compresses horizontal, vertical, and diagonal segments and leaves only their end points.
# Draw contours
cv2.drawContours(
    img, contours, -1, (0, 255, 0), 3
)  # -1 means draw all contours, (0, 255, 0) is the color in BGR format, 3 is the thickness
# Show the image

for contour in contours:
    # Filter out very small contours (noise)
    area = cv2.contourArea(contour)
    if area < 100:  # Skip contours smaller than 100 pixels
        continue

    # Calculate perimeter
    perimeter = cv2.arcLength(contour, True)

    # Try different epsilon values to find the best approximation
    approx = cv2.approxPolyDP(
        contour, 0.03 * perimeter, True
    )  # Adjusted epsilon to 0.03 for better approximation

    corners = len(approx)  # Count the number of corners

    # More accurate shape detection
    if corners == 3:
        shape = "Triangle"
    elif corners == 4:
        # Check if it's a square or rectangle
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            shape = "Square"
        else:
            shape = "Rectangle"
    elif corners == 5:
        shape = "Pentagon"
    elif corners == 6:
        shape = "Hexagon"
    elif corners > 10:
        # Check circularity for circles
        circularity = 4 * 3.14159 * area / (perimeter * perimeter)
        if circularity > 0.7:
            shape = "Circle"
        else:
            shape = "Ellipse"
    else:
        # For shapes with 7-10 corners, check if it's likely a circle
        circularity = 4 * 3.14159 * area / (perimeter * perimeter)
        if circularity > 0.7:
            shape = "Circle"
        else:
            shape = f"{corners}-sided"

    cv2.drawContours(img, [approx], 0, (255, 0, 0), 2)  # Draw the approximated polygon
    # Get the center of the contour to place the text
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv2.putText(
        img,
        shape,
        (x, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (255, 0, 0),
        2,
    )  # Put the shape name near the contour


cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
