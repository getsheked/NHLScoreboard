#weather info recovery 

#https://api.weather.gov/
#wethaer api
import configparser
import requests
import json
import weatherapi
import datetime
import keyboard

class weatherStuff:
    def __init__(self):
        self.testvar=datetime.datetime.min
        self.call1='blank'
        self.call2='blank'
        self.config=configparser.ConfigParser()
    inc=datetime.datetime.min
    def getSettings(self):
        self.config.read('config.ini')
        aws=input("Do you need to change settings? (Y/N)\n")
        if aws.upper()=='Y':
          x=input("Do you want US weather or another location? (US/N)\n")
          if x.upper()=="US":
              self.config['weather']['region']=x
          else: self.config['weather']['region']="-1"
          y=input("Enter location\n")
          self.config['weather']['location']=y
          k=input("enter key\n")
          self.config['weather']['key']=k
          t=input("C or F\n")
          if t=="C":
            self.config['weather']['units']="metric"
          else: self.config['weather']['units']="US"
          with open('config.ini', 'w') as conf:
            self.config.write(conf)    
        else: print("Using Current Settings")
    def callInfo(self):
        self.config.read('config.ini')
        key=self.config['weather']['key']
        q=self.config['weather']['location']
        future="http://api.weatherapi.com/v1/forecast.json?key="+key+"&q="+q+"&days=7&aqi=no&alerts=yes"
        return future
    def timer(self):
       if self.testvar+datetime.timedelta(seconds=45)<datetime.datetime.now():
          self.testvar=datetime.datetime.now()
          return True
    def call(self):
        if self.timer()==True:
            y=requests.get(self.callInfo())
            self.call1=y.json()
        return self.call1
    def getWeather(self):
        degre=self.config.read('config.ini')
        degre=self.config['weather']['units']
        data=self.call()
        today=datetime.datetime.today()
        d1=datetime.datetime.strftime(today+datetime.timedelta(days=1),"%Y-%m-%d")
        d2=datetime.datetime.strftime(today+datetime.timedelta(days=2),"%Y-%m-%d")
        if degre=="US":
            c=data["current"]
            current=c['temp_f'],c['condition'],c["feelslike_f"],c["wind_mph"],c["wind_dir"],c['gust_mph'],c["uv"],data['alerts']
            d1d=data["forecast"]['forecastday'][0]
            d2d=data['forecast']['forecastday'][1]
            d1Data=d1d['date'],d1d['day']["maxtemp_f"],d1d['day']["mintemp_f"],d1d['day']["maxwind_mph"],d1d['day']['condition'],d1d['day']['uv'],"'F"
            d2Data=d2d['date'],d2d['day']["maxtemp_f"],d2d['day']["mintemp_f"],d2d['day']["maxwind_mph"],d2d['day']['condition'],d2d['day']['uv'],"'F"
            return current,d1Data,d2Data
        else:
            c=data["current"]
            current=c['temp_c'],c['condition'],c["feelslike_c"],c["wind_kph"],c["wind_dir"],c['gust_kph'],c["uv"],data['alerts']
            d1d=data["forecast"]['forecastday'][0]
            d2d=data['forecast']['forecastday'][1]
            d1Data=d1d['day']['date'],d1d['day']["maxtemp_c"],d1d['day']["mintemp_c"],d1d['day']["maxwind_kph"],d1d['day']['condition'],d1d['day']["uv"],"'C"
            d2Data=d2d['day']['date'],d2d['day']["maxtemp_c"],d2d['day']["mintemp_c"],d2d['day']["maxwind_kph"],d2d['day']['condition'],d2d['day']["uv"],"'C"

            return current,d1Data,d2Data

w=weatherStuff()
print(w.getWeather()[0][0])