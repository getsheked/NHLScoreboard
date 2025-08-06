#code to push to hardware/display goes here 
from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions
from RGBMatrixEmulator import graphics
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
class imageProcessing():
    def __init__(self, rows, cols, border):
        self.buffer=border
        self.matrix=RGBMatrix(options=options)
        self.border=border
        self.dimens=(cols+(2*self.border), rows)
        self.font_s = ImageFont.load('assets/fonts/pil/Tamzen5x9r.pil')
        self.font_sb = ImageFont.load('assets/fonts/pil/Tamzen5x9b.pil')
        self.font_m = ImageFont.load('assets/fonts/pil/Tamzen6x12r.pil')
        self.font_mb = ImageFont.load('assets/fonts/pil/Tamzen6x12b.pil')
        self.font_l = ImageFont.load('assets/fonts/pil/Tamzen8x15r.pil')
        self.font_lb = ImageFont.load('assets/fonts/pil/Tamzen8x15b.pil')
        self.leftOpen=21+self.buffer
        self.colormode="RGB"
        self.image=Image.new("RGB",self.dimens)
        self.draw=ImageDraw.Draw(self.image)
    def clear(self):
        self.draw.rectangle((0, 0, self.dimens), fill=(0, 0, 0))
    def test(self):
        self.matrix.DrawText((self.leftOpen,0),"p",font=self.font_s, fill=(255, 255, 255))

x=imageProcessing(32,64,0)
x.test()
matrix.fill()
