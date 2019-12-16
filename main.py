import vpython as vp
from vpython import *

earth = vp.sphere(pos=vector(0,0,0), radius=1, texture = "http://i.imgur.com/rhFu01b.jpg", make_trail=True)
sun = vp.sphere(pos=vector(0,0,0), radius=4, texture =  "http://i.imgur.com/yoEzbtg.jpg")
t = 0

scene.autoscale = False
theta=2*3.14159/365 
EarthToSun = 50
while True:
    rate(10)
    earth.pos.x = EarthToSun*cos(t)
    earth.pos.z = EarthToSun*sin(t)
    earth.rotate(angle=theta*0.2, axis=vector(0,1,0), origin=vector(0,0,0))
    sun.rotate(angle=theta*0.2, axis=vector(0,1,0), origin=vector(0,0,0))
    t+=0.01
