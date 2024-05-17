import cv2 as cv 
import numpy as np 
from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input, decode_predictions

model=ResNet50(weights='imagenet')
img=cv.imread('rabbit.jpg')
x-np.reshape(cv.resize(img, (224,224)), (1,224,224,3))
x=preprocess_input(x)
preds model-predict(x)
top5-decode_predictions(preds, top=5)[0]
print('예측 결과:',top5)
for i in range(5):
cv-putText(img,top5[i][1]+':'+str(top5[i][21),(10,20+i*20),cv.FONT_HERSHEY_
SIMPLEX,0.5, (255,255,255),1)
17
18
19
20
cv.imshow('Recognition result',img)
cv.waitKeyO
21 cv-destroyAllWindows)