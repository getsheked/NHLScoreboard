from setup import teaminfo
from datetime import datetime
import requests 
teaminfo=teaminfo()

def scoreboardCall(x):
    response=requests.get("https://api-web.nhle.com/v1/gamecenter/"+str(x)+"/boxscore")
    data=response.json()
    return data
def getGameIDs():
    x=-1
    y=-1
    z=-1
    for i in range(len(teaminfo.gameList)):
        if teaminfo.gameList[i][0]==datetime.today().date():
            x=teaminfo.gameList[i][1]
            if i+1>(len(teaminfo.gameList)-1):
                y=-1
            else: y=teaminfo.gameList[i+1][1]
            if i-1<0:
                z=-1
            else: z=teaminfo.gameList[i-1][1]
            return x,y,z   
        elif teaminfo.gameList[i][0]>datetime.today().date():
            x=teaminfo.gameList[i][1]
            if i-1<0:
                z=-1
            else: z=teaminfo.gameList[i-1][1]
            return x,y,z           
def timeProcess(x):
    offset=teaminfo.timeInfo
    t=datetime.strptime(x,"%Y-%m-%dT%H:%M:%S%z")
    if offset[1]=='-':
        time=t-offset[0]
    else: time=t+delta
    time=time.strftime("%m-%d %-I:%M %p")
    return time[0:5],time[6:]

        #(scheudlestate(gametype,gamedate,gamestart,homeaway?)(favabbrev,favscore)(awayscore,awayabrev)(state,period,intermission?)
def processgameID(x):
    gameType=-1
    homeAway=-1
    favScore=-1
    favAbv=teaminfo.teamAbv
    otherAbv=-1
    otherScore=-1
    gameState=-1
    period=-1
    inter=-1
    time=-1
    at=-1
    
    data=scoreboardCall(x)
    gameType=data['gameType']
    timeInfo=timeProcess(data['startTimeUTC'])
    gameState=data['gameState']
    if data['homeTeam']['abbrev']==favAbv:
        homeAway="home"
        at="vs"
    else:
        homeAway="away"
        at="at"
    if homeAway=="home":
        otherAbv=data['awayTeam']['abbrev']
        if data['gameState']!='FUT':
            favScore=data['homeTeam']['score']
            otherScore=data['awayTeam']['score']
            period=data['periodDescriptor']['number']
            time=data['clock']['timeRemaining']
            inter=data['clock']['inIntermission']
        else:
            favScore=-1
            otherScore=-1
    else:
        otherAbv=data['homeTeam']['abbrev']
        if data['gameState']!='FUT':
            favScore=data['awayTeam']['score']
            otherScore=data['homeTeam']['score']
            period=data['periodDescriptor']['number']
            time=data['clock']['timeRemaining']
            inter=data['clock']['inIntermission']
        else:
            favScore=-1
            otherScore=-1
    return ((gameType,at),timeInfo,(favAbv,favScore),(otherAbv,otherScore),(gameState,period,inter,time))
def displayProcessing(x):
    print(x)
    score1=x[2][1]
    displayMode=-1
    score2=x[3][1]
    middleText=-1
    periodText=-1
    date=x[1][0]
    team1abv=x[2][0]
    team2abv=x[3][0]
    gameState=x[4][0]
    period=x[4][1]
    inter=x[4][2]
    time=x[4][3]
    gameType=x[0][0]
    
    if gameState != "FUT":
        displayMode=1
        if gameType==1:
            if inter==False:
                if period<=3:
                    periodText=period
                else: periodText="SO"
            else: periodText= str(period)+'INT'
        elif gameType==2:
            if inter==False:
                if period<=3:
                    periodText=period
                elif period==4:
                    periodText="OT"
                else: periodText="SO"
            else: periodText= str(period)+'INT'
        else:
            if inter==False:
                if period<=3:
                    periodText=period
                else:
                    if (period-3)>=8:
                        periodText=str(period-3)+'OT'
                    else: periodText='OT'
            else: periodText= str(period)+'INT'
    if gameState == "OFF":
        middleText='FINAL'
    if gameState != "OFF" and gameState != "FUT":
        middleText=time
    if gameState == "FUT":
        displayMode==2
        score1=x[1][0]
        score2=x[1][1]    
    return displayMode,date,score1,team1abv,score2,team2abv,middleText,periodText