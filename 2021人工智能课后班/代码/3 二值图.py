import cv2
camera = cv2.VideoCapture(0)
num = 0
while True:
    turn,image = camera.read()
    color = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    re,binary = cv2.threshold(color,150,255,2)#threshold n.门槛 传参：src：灰度图   thresh：亮度；
                                    #maxval；int.未知(255)   dst：int.是否取反(0)
    cv2.imshow("yeeeeeeeee",binary)
    if cv2.waitKey(1) >= 1:
        break
cv2.destroyAllWindows()
camera.release()
