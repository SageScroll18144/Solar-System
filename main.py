import vpython as vp
from vpython import *

earth = vp.sphere(pos=vector(50,0,0), radius=1, texture = "http://i.imgur.com/rhFu01b.jpg", make_trail=True)
sun = vp.sphere(pos=vector(0,0,0), radius=4, texture =  "http://i.imgur.com/yoEzbtg.jpg")
t = 0

scene.autoscale = False
theta=2*3.14159/365 #vel ang

while True:
    rate(60)

    earth.rotate(angle=theta, axis=vector(0,1,0), origin=vector(0,0,0))
     
    t+=0.01
    


