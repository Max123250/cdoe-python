import cv2
img = cv2.imread("image/01.png")
for i in range(10):
    cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()