import cv2
img = cv2.imread("image.png")          # load
cv2.imshow("Original", img)            # display
cv2.waitKey(0)
ok = cv2.imwrite("image2.png", img)  # save
print("Saved:", ok)
cv2.destroyAllWindows()