import os
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import requests
import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from configparser import ConfigParser
from setup import teaminfo
import infogetter

options = RGBMatrixOptions()
options.rows = 32
options.cols= 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options = options)

blue = graphics.Color(0, 0, 255)
white=white = graphics.Color(255, 255, 255)

font1= graphics.Font()
font1.LoadFont("/home/nhlpi9/dev/nhl/src/graphicFont/bdf-fonts/5x7.bdf")
font2= graphics.Font()
font2.LoadFont("/home/nhlpi9/dev/nhl/src/graphicFont/bdf-fonts/6x9.bdf")
font3= graphics.Font()
font3.LoadFont("/home/nhlpi9/dev/nhl/src/graphicFont/bdf-fonts/spleen-12x24.bdf")

#if x[0]==0:
    #time left
   # graphics.DrawText(matrix, font2, 18, 18, white, x[1][5])
    
    #period
    #graphics.DrawText(matrix, font2, 30, 27, white, str(period))
    
    #home score
    #graphics.DrawText(matrix, font3, 4, 28, white,str(x[1][2]))

    #home name
   # graphics.DrawText(matrix, font2, 3, 10, white,str(x[1][1]))
    
    #away score
    #graphics.DrawText(matrix, font3, 50, 28, white,str(x[1][4]))
    
    #away name
   # graphics.DrawText(matrix, font2, 45, 10, white,str(x[1][3]))
   
#return displayMode,score1,team1abv,score2,team2abv,middleText,periodText
def displayMode1(x):
    print(x)
def displayMode2(x):
   print(x)
x=infogetter.getGameIDs()
for i in range(len(x)):
    if x[i]>0:
        print(infogetter.processgameID(x[i]))
        y=infogetter.processgameID(x[i])
        while y[4][0]!= "OFF" and y[4][0]!= "FUT":
            y=infogetter.processgameID(x[i])
            infogetter.displayProcessing(y)
            displayMode1(infogetter.displayProcessing(y))
        if y[4][0]== "OFF":
            y=infogetter.processgameID(x[i])
            infogetter.displayProcessing(y)
            displayMode1(infogetter.displayProcessing(y))
        elif y[4][0]=="FUT":
            y=infogetter.processgameID(x[i])
            infogetter.displayProcessing(y)
            displayMode2(infogetter.displayProcessing(y))
                
        