import cv2,winsound
cap = cv2.VideoCapture(700)
detector = cv2.CascadeClassifier("model/face.xml")
while True:
    ret,img = cap.read()
    faces = detector.detectMultiScale(img,1.2,7)
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x + w,y + h),(0,255,0),3)
        winsound.Beep(1000,100)
    cv2.imshow("video",img)
    if cv2.waitKey(10) > 1:
        break
cv2.destroyAllWindows()
cap.release()
