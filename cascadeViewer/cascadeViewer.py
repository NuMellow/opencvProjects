import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

#capture web cam footage
cap = cv2.VideoCapture(0)

print ("###################################")
print ("### CASCADE VIEWER v0.2 ###########")
print ("#################### by NuMellow ##")
print ("###################################")

print

print ("n - open new cascade")
print ("t - change the threshold value")
print ("q - quit")


#gets the cascade file from the dialog box
print("Please select cascade file")
cascPath = filedialog.askopenfilename()

objCascade = cv2.CascadeClassifier(cascPath)

threshold = 2

def changeCascade(): #This allows you to change the cascade file. (Be sure to select a cascade file or else it will crash. probably. Definitely.)
	global cascPath 
	global objCascade
	cascPath = filedialog.askopenfilename()
	objCascade = cv2.CascadeClassifier(cascPath)

def changeThreshold(): #This function allows you to change the threshold applied to the cascade. Remember it works with even numbers
	global threshold
	threshold = raw_input("Enter threshold value: ")
	threshold = int(threshold)
	
while True:
	#Just some debugging stuff
	#print(threshold)
	
	t = threshold
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	obj = objCascade.detectMultiScale(gray, t, t)
	
	for (x,y,w,h) in obj:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
		
	cv2.imshow('cascade viewer', frame)

	if cv2.waitKey(1) & 0xff == ord('q'):
		break
		
	if cv2.waitKey(1) & 0xff == ord('n'):
		changeCascade()
		
	if cv2.waitKey(1) & 0xff == ord('t'):
		changeThreshold()
		
cap.release()
cv2.destroyAllWindows()		
