# -*- coding: utf-8 -*-
"""faceDetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aEgiF8k5glALFy2CD0FDcbiyEe5jEroR
"""

import numpy as np
import cv2
from google.colab.patches import cv2_imshow

# Globals
FACE_CLASSIFIER = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
EYE_CLASSIFIER = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
SCALE_FACTOR = 1.3
BLUE_COLOR = (255, 0, 0)
MIN_NEIGHBORS = 5

img = cv2.imread('image1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img

faces = FACE_CLASSIFIER.detectMultiScale(gray)

faces

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = EYE_CLASSIFIER.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0),2)

cv2_imshow(img)
#.waitKey(0)
#cv2.destroyAllWindows()

