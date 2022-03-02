import cv2
camera = cv2.VideoCapture(0)
num = 0
while True:
    turn,image = camera.read()
    cv2.imshow("yeeeeeeeee",color)
    if cv2.waitKey(1) >= 1:
        break
cv2.destroyAllWindows()
camera.release()
