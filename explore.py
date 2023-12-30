import sys
import os
from PIL import Image
import pytesseract
from pytesseract import image_to_string
from pytesseract import image_to_data

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\cassa\AppData\Local\Programs\Tesseract-OCR\tesseract.exe" 

"""
Set the Folder Paths
"""
PROJECT_PATH = os.path.abspath(os.path.split(sys.argv[0])[0])
DIR_ABS = os.path.dirname(os.path.abspath(__file__))
DIR_IMAGES = os.path.join(PROJECT_PATH, 'images')
DIR_OUTPUT = os.path.join(PROJECT_PATH, 'output')


"""
Assign Installed Path (for windows machine.)
"""
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img_text = None
try:
	file_path = os.path.join(DIR_IMAGES ,"image_2.jpg")
	
	if os.path.isfile(file_path):
		img_obj = Image.open(file_path)
		img_text = image_to_string(img_obj)
	else:
		pass
except Exception as e:
	print(str(e))



# Final Result 
if img_text:
	# write the image texts to the ouput file


	try:
		""" 
		Check if Output directory Exists, If not, Create the directory
		"""
		if not os.path.exists(DIR_OUTPUT):
			os.makedirs(DIR_OUTPUT)

		""" Write Image Text to the file """
		output_file = open(DIR_OUTPUT +"/output_2.txt", "w") 
		output_file.write(img_text) 
		output_file.close() 

	except Exception as e:
		raise e
	print(img_text)