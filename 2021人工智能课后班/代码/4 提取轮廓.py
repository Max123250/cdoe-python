import cv2
camera = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier("model/face.xml")
while True:
    turn,image = camera.read()
    color = cv2.cvtColor(image,6)
    re,binary = cv2.threshold(color,150,255,1)
    cnts,layers = cv2.findContours(binary,3,2)
    for cnt in cnts:
        x,y,w,h = cv2.boundingRect(cnt)#计算轮廓外接矩形
        if not (35 < w < 100 or 35 < h < 100):
            continue
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("binary",binary)
    cv2.imshow("image",image)
    if cv2.waitKey(1) >= 1:
        break
cv2.destroyAllWindows()
camera.release()
