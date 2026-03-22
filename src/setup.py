
import os
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import requests
import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from configparser import ConfigParser

class teaminfo:
    config=ConfigParser()
    config.read('config.ini') 
    teamID=int(config.get('team','teamID'))
    teamAbv=config.get('team', 'teamabv')
    timeFormat=int(config.get('time','24hr'))
    offset=datetime.now().astimezone()
    x=datetime.strftime(offset,"%z")
    z=x[2:3]
    y=x[3:5]
    delta=timedelta(hours=int(z),minutes=int(y))
    timeInfo=delta,x[0]
    response=requests.get("https://api-web.nhle.com/v1/club-schedule-season/"+teamAbv+"/now")
    data=response.json()
    gameList=[]
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
    font1.LoadFont("/home/nhlpi9/dev/nhl/src/graphicFont/bdf-fonts/4x6.bdf")
    font2= graphics.Font()
    font2.LoadFont("/home/nhlpi9/dev/nhl/src/graphicFont/bdf-fonts/6x9.bdf")
    font3= graphics.Font()
    font3.LoadFont("/home/nhlpi9/dev/nhl/src/graphicFont/bdf-fonts/spleen-12x24.bdf")
    for i in range(len(data['games'])):
            y=data['games'][i]['id']
            x=data['games'][i]['gameDate']
            x=datetime.strptime(x,"%Y-%m-%d").date()
            entry=[x,y]
            gameList.append(entry)
