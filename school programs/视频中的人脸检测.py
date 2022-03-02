import cv2
cap = cv2.VideoCapture(700)
detector = cv2.CascadeClassifier("model/face.xml")
while True:
    ret,img = cap.read()
    re,binary = cv2.threshold(img,150,255,2)
    faces = detector.detectMultiScale(img,1.2,6)
    for x,y,w,h in faces:
        cv2.rectangle(img,(x-20,y-70),(x+w+20,y+h+50),(0,255,0),3)
    cv2.imshow("video",binary)
    if cv2.waitKey(10) > 1:
        break
cv2.destroyAllWindows()
cap.release()
