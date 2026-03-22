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

#if x[0]==0:
    #time left
   # graphics.DrawText(matrix, font2, 18, 18, white, x[1][5])
    
    #period
    #graphics.DrawText(matrix, font2, 30, 27, white, str(period))
    
    #home score
    #graphics.DrawText(matrix, font3, 4, 28, white,str(x[1][2]))

    #home name
   #graphics.DrawText(matrix, font2, 3, 10, white,str(x[1][1]))
    
    #away score
    #graphics.DrawText(matrix, font3, 50, 28, white,str(x[1][4]))
    
    #away name
   # graphics.DrawText(matrix, font2, 45, 10, white,str(x[1][3]))

def displayMode1(x):
    teaminfo.matrix.Clear()
    graphics.DrawText(teaminfo.matrix, teaminfo.font1, 23, 15, teaminfo.white,str(x[1]))	
    graphics.DrawText(teaminfo.matrix, teaminfo.font3, 5, 28, teaminfo.white,str(x[2]))
    graphics.DrawText(teaminfo.matrix, teaminfo.font1, 5, 8, teaminfo.white,str(x[3]))
    graphics.DrawText(teaminfo.matrix, teaminfo.font3, 50, 28, teaminfo.white,str(x[4]))
    graphics.DrawText(teaminfo.matrix, teaminfo.font1, 50, 8, teaminfo.white,str(x[5]))
    graphics.DrawText(teaminfo.matrix, teaminfo.font1, 24, 23, teaminfo.white,str(x[6]))
    graphics.DrawText(teaminfo.matrix, teaminfo.font1, 30, 30, teaminfo.white,str(x[7]))
    time.sleep(3)
    clock()
def displayMode2(x):
    print(x)
    teaminfo.matrix.Clear()
    graphics.DrawText(teaminfo.matrix, teaminfo.font1, 30, 8, teaminfo.white,str(x[0][1]))	
    graphics.DrawText(teaminfo.matrix, teaminfo.font2, 8, 8, teaminfo.white,str(x[2][0]))
    graphics.DrawText(teaminfo.matrix, teaminfo.font2, 43, 8, teaminfo.white,str(x[3][0]))
    graphics.DrawText(teaminfo.matrix, teaminfo.font2, 5, 18, teaminfo.white,str(x[1][0]))
    graphics.DrawText(teaminfo.matrix, teaminfo.font2, 20, 28, teaminfo.white,str(x[1][1]))
    time.sleep(3)
def clock():
    for i in range(120):
        teaminfo.matrix.Clear()
        now=datetime.now()
        if teaminfo.dateFormat=='D':
            date=now.strftime("%B %d")
        else: date=now.strftime("%d %B")
        if teaminfo.timeFormat==24:
            timef=now.strftime("%H:%M")
            graphics.DrawText(teaminfo.matrix,teaminfo.font3,3,20,teaminfo.white,timef)
        else:
            timef=now.strftime("%I:%M")
            graphics.DrawText(teaminfo.matrix,teaminfo.font3,3,20,teaminfo.white,timef)
            graphics.DrawText(teaminfo.matrix,teaminfo.font2,50,31,teaminfo.white,now.strftime("%p"))
        graphics.DrawText(teaminfo.matrix,teaminfo.font5,2,31,teaminfo.white,date)
        time.sleep(0.5)
while 1<2:
    x=infogetter.getGameIDs()
    for i in range(len(x)):
        if x[i]>0:
            y=infogetter.processgameID(x[i])
            while y[4][0]!= "OFF" and y[4][0]!= "FUT":
                y=infogetter.processgameID(x[i])
                displayMode0(infogetter.displayProcessing(y))
            if y[4][0]== "OFF":
                y=infogetter.processgameID(x[i])
                displayMode1(infogetter.displayProcessing(y))
                i=i+1
            if y[4][0]=="FUT":
                y=infogetter.processgameID(x[i])
                displayMode2(infogetter.processgameID(x[i]))
                i=i+1
            
        
