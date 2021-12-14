import numpy as np
import cv2 as cv

from criminalController import add_criminal_location
from util.criminaldata import get_criminal_labels

from util.config import get_haar_cascade_path
from util.config import get_storage_path
from util.config import get_trained_model_path
from util.config import get_criminal_labels

capture=""

def face_recognition(db):
    print("In Face Recognition func")
    # haar_cascade_path=r"C:\Users\Welcome\Desktop\MiniProject\ScamProject\Resources\HaarCascadeFiles\haarcascade_frontalface_default.xml"
    haar_cascade_path=get_haar_cascade_path()
    haar_cascade = cv.CascadeClassifier(haar_cascade_path)

   
    trained_model_path = get_trained_model_path()

    # criminals = ["18H61A05J4","18H61A05K1","18H61A05L0","18H61A05M0","18H61A05M3","18H61A05N3","18H61A05N5","18H61A05N6","18H61A05N7","19H65A0520"]
    criminals = get_criminal_labels()
   
    
    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read(trained_model_path)

  
    capture=cv.VideoCapture(0)

  
    capture.set(3,600)
   
    capture.set(4,500)

    while True:
        isTrue,frame=capture.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
       
        faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

        for (x,y,w,h) in faces_rect:
           
            faces_roi = gray[y:y+h,x:x+w]

            
            label, confidence = face_recognizer.predict(faces_roi)
            print(f'Label = {criminals[label]} with a confidence of {confidence}')
           
            cv.putText(frame, str(criminals[label]), (x,y+10), cv.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), thickness=1)
            cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)
            add_criminal_location(db,criminals[label],"hyderabad")    
        cv.imshow('Detected Face', frame)

        if(cv.waitKey(20) & 0xFF==ord('x')):
            cv.destroyAllWindows()
            capture.release()
            break
            
def stop_recognition():
    cv.destroyAllWindows()
    capture.release()
