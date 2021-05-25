#!/usr/bin/env python
import time
import json
import urllib.request
from datetime import datetime
from datetime import timedelta
import turtle

n0=datetime.now()
td=input("Define time: ")

l=len(td)
if td[l-1].upper()=='H':
    td=int(td[:-1])*3600
elif td[l-1].upper()=='M':
    td=int(td[:-1])*60
elif td[l-1].upper()=='S':
    td=int(td[:-1])
elif int(td[l-1])>=0 and int(td[l-1])<10:
    td=int(td)
else:
    print('Erro')
print(td)
n1=n0+timedelta(seconds=td)

print(n1)

nn=datetime.now()

t=turtle.Turtle()
t.color("red")
turtle.setup(1600,800)
screen=turtle.Screen()
screen.bgpic('earth.gif')
#screen.addshape('ship.png')
#t.shape('ship.png')
screen.setup(1080,540)
t.penup()
lonAnt=[]
while nn<n1:
    dtTime=time.strftime("%y-%m-%d %H:%M:%S")
    locales="http://api.open-notify.org/iss-now.json"
    respLocs=urllib.request.urlopen(locales)

    nn=datetime.now()
    resultL=json.loads(respLocs.read())
    pos=resultL['iss_position']
    lat=pos['latitude']
    lon=pos['longitude']
    tst=resultL['timestamp']
    print(lon,lat)
    lat=float(lat)*3
    lon=float(lon)*3
    if len(lonAnt)>0:
        print(lon-lonAnt[0])
        if lon-lonAnt[0]>10 or lon-lonAnt[0]<-10:
            t.penup()
    lonAnt=[]
    lonAnt.append(lon)
    t.setpos(lon,lat)
    t.pendown()
    t.setpos(lon,lat)
    time.sleep(2)
    
