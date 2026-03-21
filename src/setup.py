
import os
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import requests
import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
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
    for i in range(len(data['games'])):
            y=data['games'][i]['id']
            x=data['games'][i]['gameDate']
            x=datetime.strptime(x,"%Y-%m-%d").date()
            entry=[x,y]
            gameList.append(entry)
