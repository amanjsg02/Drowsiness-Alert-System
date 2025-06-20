import cv2
import numpy as np

import tensorflow as tf

import pygame
import time
import dlib



cnn=tf.keras.models.load_model('drowziness_model2.h5')


pygame.mixer.init()
pygame.mixer.music.load("AlarmTone.mp3")





cap=cv2.VideoCapture(0)

ret,frame=cap.read()
import cv2

# Create tracker from cv2.legacy
tracker = cv2.legacy.TrackerCSRT_create()
check=0
no_face_check=0
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def pic_show(frame,roi1):
    global check,no_face_check
    a,b,wid,height=tuple(map(int,roi1))
    h, w = frame.shape[:2]
    if a < 0 or b < 0 or a + wid > w or b + height > h:
        print("ROI is out of frame bounds. Skipping this frame.")
        return
    

    mask=frame[b:b+height,a:a+wid]
    if mask.size == 0:
        print("Mask is empty. Skipping frame.")
        return
    
    mask=cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
    faces1=detector(mask)
    
    if(len(faces1)!=0):
         no_face_check=0
         if pygame.mixer.get_busy():
             pygame.mixer.music.stop()
            
         
         mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2RGB)
         mask=mask/255.0
         mask=cv2.resize(mask,(64,64))
         mask=np.expand_dims(mask, axis=0)
         result=cnn.predict(mask,verbose=0)
         
         mask=np.squeeze(mask,axis=0)
         if (result[0][0]<0.25):
            print(result[0][0])
                 
                 
            check=check+1
                
            time.sleep(0.1)
            if (check>=3):
                if not pygame.mixer.get_busy():
                    pygame.mixer.music.play(-1)
                           
                     
         else:
          check=0
          if pygame.mixer.music.get_busy():
             pygame.mixer.music.stop()
                
             
        
        
         
    else:
         print("No Face Detected")
       
         no_face_check=no_face_check+1
         time.sleep(0.3)
         if(no_face_check>=3):
             if not pygame.mixer.music.get_busy():
                 pygame.mixer.music.play(-1)
            
             
        
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

# Select ROI (interactive window may not show in Spyder IDE)
roi = cv2.selectROI("Select ROI", frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("Select ROI")

# Initialize tracker
tracker.init(frame, roi)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    success, roi = tracker.update(frame)
    x, y, w, h = tuple(map(int, roi))

    if success:
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        pic_show(frame, roi)
    else:
        cv2.putText(frame, "Tracking failure", (100, 200),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
       

    cv2.imshow("Tracking", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




