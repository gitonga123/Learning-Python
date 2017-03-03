import tesserocr
from PIL import Image

print tesserocr.tesseract_version()  # print tesseract-ocr version
print tesserocr.get_languages()  # prints tessdata path and list of available languages

image = Image.open('4.jpg')
print tesserocr.image_to_text(image)  # print ocr text from image
# or
daniel= tesserocr.file_to_text('4.jpg')

print "This is the text to be displayed"
print daniel.split()