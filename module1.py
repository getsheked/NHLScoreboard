#weather info recovery 

#https://api.weather.gov/
#wethaer api
import configparser 


class weatherstuff():
    def getSettings(self):
        config=configparser.ConfigParser()
        config.read('config.ini')
        aws=input("Do you need to change settings? (Y/N)\n")
        if aws.upper()=='Y':
          w=input("Do you want US weather or another location? (US/N)\n")
          if w.upper()=="US":
              config['weather']['region']="US"
          else: config['weather']['region']="-1"
          x=input("Enter Post/ZIP code\n")
          config['weather']['location']=x
          y=input("Enter API Key")
          config['weather']['key']=y
          with open('config.ini', 'w') as conf:
            config.write(conf)   
        else: print("Using Current Settings")


w=weatherstuff()

w.getSettings()


