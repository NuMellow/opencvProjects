import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

cap =cv2.VideoCapture(0)

#gets the cascade file from the dialog box
print("Please select cascade file")
cascPath = filedialog.askopenfilename()

objCascade = cv2.CascadeClassifier(cascPath)

def changeCascade():
	global cascPath 
	global objCascade
	cascPath = filedialog.askopenfilename()
	objCascade = cv2.CascadeClassifier(cascPath)

while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	obj = objCascade.detectMultiScale(gray)
	
	for (x,y,w,h) in obj:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
		
	cv2.imshow('cascade viewer', frame)

	if cv2.waitKey(1) & 0xff == ord('q'):
		break
		
		
	if cv2.waitKey(1) & 0xff == ord('n'):
		changeCascade()
		
cap.release()
cv2.destroyAllWindows()		
