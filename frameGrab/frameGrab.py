import cv2
import os
import sys

source = ""
destination = ""

def show_options():
	print("1. Enter source file")
	print("2. Enter output folder")
	print("3. Run")
	print(" -More features coming soon- ")
	print("q. Exit")
	print
	
def get_source_file():
	global source
	
	while len(source) < 1:
		source = input("Enter video file: ")
	
	
def get_destination_folder():
	global destination
	
	while len(destination) < 1:
		destination = input("Enter folder name: ")
	
	if not os.path.exists(destination):
		os.makedirs(destination)
		
def check_source():
	global source
	
	if len(source) == 0:
		return False
	else:
		return True
		
def run_prog():
	global source
	global destination
	
	frame_num = 1
	
	cap = cv2.VideoCapture(source)
	
	while cv2.waitKey(1) < 0:
		ret, frame = cap.read()
		if not ret:
			break
		
		cv2.imwrite(destination + "/" + str(frame_num) + '.jpg', frame)
		frame_num += 1
			
		cv2.imshow('frameGrab', frame)	
		
	cap.release()
	cv2.destroyAllWindows()
	
	print("Completed")
	
	
	
	
	

def main(argv):	

	global source
	global destination
	
	#Wlcome message and main menu
	print
	print("####################")
	print("####################")
	print("#### FRAME GRAB ####")
	print("########by Chisulo##")
	print("####################")
	print("####################")
	print
	
	if len(argv) == 0:
		
		show_options()
		option = input("Select option: ")
	
		while True:
			if option == "1":
				print("ENTER SOURCE FILE")
				print
				get_source_file()
			elif option == "2":
				print("ENTER DESTINATION FOLDER")
				print
				get_destination_folder()
			elif option == "3":
				if check_source():
					run_prog()
				else:
					print("Missing source file")
			elif option == "q":
				break
			else:
				print("Please select from the available options")
				show_options()
				
			option = input("Select option: ")	
			

if __name__ == "__main__":
	main(sys.argv[1:]) #sends command line arguments to main method. Excludes program name
	

