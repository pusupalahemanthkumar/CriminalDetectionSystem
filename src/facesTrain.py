import os
import cv2 as cv
import numpy as np
from util.config import get_criminal_labels

from util.config import get_haar_cascade_path
from util.config import get_storage_path
from util.config import get_trained_model_path_folder

# criminals = ["18H61A05J4","18H61A05K1","18H61A05L0","18H61A05M0","18H61A05M3","18H61A05N3","18H61A05N5","18H61A05N6","18H61A05N7","19H65A0520"]
criminals = get_criminal_labels()

DIR =get_storage_path()

# haar_cascade_path=r"C:\Users\Welcome\Desktop\MiniProject\ScamProject\Resources\HaarCascadeFiles\haarcascade_frontalface_default.xml"
haar_cascade_path= get_haar_cascade_path()

trained_model_path=get_trained_model_path_folder()


haar_cascade = cv.CascadeClassifier(haar_cascade_path)


features = []
labels = []

def create_train():
    for person in criminals:

        path = os.path.join(DIR, person)
        label = criminals.index(person)

        for img in os.listdir(path):

            img_path = os.path.join(path,img)
            img_array = cv.imread(img_path)

            if img_array is None:
                continue 
                
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

print("---------------------- Started Training ----------------------")
create_train()
print('----------------------- Training done ------------------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features,labels)

face_recognizer.save(os.path.join(trained_model_path, 'face_trained.yml'))
np.save(os.path.join(trained_model_path, 'features.npy'), features)
np.save(os.path.join(trained_model_path, 'labels.npy'), labels)
