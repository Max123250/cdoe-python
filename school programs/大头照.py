import cv2
cap = cv2.VideoCapture(0)
fcc = cv2.VideoWriter_fourcc(*"XVID")
#video = cv2.VideoWriter("video/video.avi",fcc,100.0,(640,480),True)
detector = cv2.CascadeClassifier("model/face.xml")
while True:
    ret,img = cap.read()
    img = cv2.flip(img,1)
    faces = detector.detectMultiScale(img,1.2,6)
    for face in faces:
        x,y,w,h = face
        for i in range(len(face)):
            if face[i] >= 0:
                img = img[y:y + h,x:x + w]
    #video.write(img)
    cv2.imshow("video",img)
    if cv2.waitKey(10) > 1:
        break
cv2.destroyAllWindows()
cap.release()
video.release()
