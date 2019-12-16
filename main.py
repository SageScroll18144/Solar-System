import vpython as vp
from vpython import *

earth = vp.sphere(pos=vector(10,0,0), radius=1, texture = "http://i.imgur.com/rhFu01b.jpg", make_trail=True)
t = 0

scene.autoscale = False
theta=2*3.14159/365 #vel ang
omega=2*3.14159/28
while True:
    rate(60)

    earth.rotate(angle=theta, axis=vector(0,1,0), origin=vector(0,0,0))
    #earth.pos.y = sin(t)
    #earth.pos.x = cos(t)
    # earth.pos = vec( astronomicalUnit * cos(radians(earthAngle)), 0, astronomicalUnit * sin(radians(earthAngle)) )
    print(sin(t), end='\t')
    print(cos(t))
    
    t+=0.01
    


