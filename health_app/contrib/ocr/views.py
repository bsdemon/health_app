from PIL import Image
import pytesseract

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def image(request):
    pass




# pytesseract.pytesseract.tesseract_cmd = '<full_path_to_your_tesseract_executable>'
# Include the above line, if you don't have tesseract executable in your PATH
# Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

# print(pytesseract.image_to_string(Image.open('test.png')))
# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))


# #Add the following config, if you have tessdata error like: "Error opening data file..."
# tessdata_dir_config = '--tessdata-dir "<replace_with_your_tessdata_dir_path>"'
# # Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# # It's important to add double quotes around the dir path.

# pytesseract.image_to_string(image, lang='chi_sim', config=tessdata_dir_config)