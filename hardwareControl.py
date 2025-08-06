#code to push to hardware/display goes here 
from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions, graphics
from NHLv2 import *
from PIL import Image, ImageDraw, ImageFont

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
matrix = RGBMatrix(options = options)
rows=32
cols=64 
DIMS=(cols, rows)
image=Image.new('RGB',DIMS)
draw=ImageDraw.Draw(image)


font = ImageFont.truetype("arial.ttf", 10)

draw.rectangle(((0, 0),DIMS), fill=(125,0,0,0))
draw.text((0, 10), "NHL Game Info", font=font, fill=(255, 255, 255))
matrix.SetImage(image)