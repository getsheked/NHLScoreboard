#code to push to hardware/display goes here 
import configparser
from encodings.punycode import selective_find
from mailbox import NoSuchMailboxError
from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions
import RGBMatrixEmulator
from RGBMatrixEmulator.emulation.options import RGBMatrixEmulatorConfig
from RGBMatrixEmulator.graphics import *
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta, timezone, time, date

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
class deterimineDisplay():
        def __init__(self,gameOn,gameState,period,favScore,favShots,otherID,otherScore,otherShots,gameTime,lastgame,nextgame):
            self.gameON=gameOn
            self.gameState=gameState
            self.period=period
            self.favScore=favScore
            self.favShots=favShots
            self.otherID=otherID
            self.otherScore=otherScore
            self.otherShots=otherShots
            self.gameTime=gameTime
            self.lastgame=lastgame
            self.nextgame=nextgame
            self.font1=RGBMatrixEmulator.Font()
            self.font2=RGBMatrixEmulator.Font()
            self.font4=RGBMatrixEmulator.Font()
            self.dimens=(64,32)
            self.matrix=RGBMatrix(options=options)
            self.image=Image.new("RGB",self.dimens)
            self.draw=ImageDraw.Draw(self.image)
            self.time=time
            self.date=date
        def selectScreen(self):
            if self.gameState!= "OFF" or -1:
                return 0 #clock
            if self.gameState!="FUT" or -1:
                if self.gameState=="CRIT" or "LIVE":
                    return 1
            if self.gameState=="FUT":
                return 2
        def DisplayClock(self):
            if int(self.time) == 12:
                FormatCode = "%I:%M %p"
            else: FormatCode= "%H:%M"
            return datetime.now().strftime(FormatCode)
        def DisplayDate(self):
            if self.date== 'M':
               DateCode="%a, %b %e"
            else: DateCode="%a,%e %b"
            return datetime.now().strftime(DateCode)
        def setFonts(self):
            config=configparser.ConfigParser()
            config.read("config.ini")
            x=config.get('text','font')
            font=RGBMatrixEmulator.Font()
            self.time=config.get('time','24hr')
            self.date=config.get('time','seconddigit')
            self.font1=font.LoadFont("assets\\fonts\\6x10.bdf")
            self.font2=font.LoadFont("assets\\fonts\\LEDBOARD-8pt.bdf")
        def screen0(self):
            self.draw.rectangle(((0,0),(self.dimens[0], self.dimens[1])), fill=(0,50, 0, 255))
            print(self.time)
            if self.DisplayClock()[-1:]=="M":
                print("12 Hour Format")
                self.draw.text((16, 16), self.DisplayClock()[-2:], font=self.font2, fontsize=20,fill=(255, 255, 255, 255), anchor="mb")
            
            #self.draw.text((32, 16), time, font=self.font1, font_size=20, fill=(255, 255, 255,255), anchor="mb")
            self.matrix.SetImage(self.image)
