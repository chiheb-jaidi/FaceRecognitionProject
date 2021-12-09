import RPi.GPIO as GPIO   #import library to access GPIO PIN
import time   #to access delay function 
import cv2
from simple_facerec import SimpleFacerec

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
DC_Motor_Pin1=17  #define pin for dc motor
DC_Motor_Pin2=27 #define pin for dc motor
GPIO.setup(DC_Motor_Pin1,GPIO.OUT) #set pin function as output
GPIO.setup(DC_Motor_Pin2,GPIO.OUT) #set pin function as output

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")
   
while(1):
  
    # Load Camera
    cap = cv2.VideoCapture(2)
    for face_loc, name in zip(face_locations, face_names):
        ref=false
    if re==false:
        GPIO.output(DC_Motor_Pin1,GPIO.HIGH)
        GPIO.output(DC_Motor_Pin2,GPIO.LOW) 
