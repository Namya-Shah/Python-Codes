from csv import writer
import barcode
from barcode.writer import ImageWriter

text = "Python programming code to generate barcode"
text1 = str(text)
code = barcode.get_barcode_class("code128")
image = code(text, writer = ImageWriter())
save_img = image.save('myfinalbarcode')