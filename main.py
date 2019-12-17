import vpython as vp
from vpython import *

earth = vp.sphere(pos=vector(0,0,0), radius=1, texture = "http://i.imgur.com/rhFu01b.jpg", make_trail=False)
sun = vp.sphere(pos=vector(0,0,0), radius=4, texture =  "http://i.imgur.com/yoEzbtg.jpg")
moon = vp.sphere(pos=vector(0, 0.5,0),radius=0.5, texture = "http://i.imgur.com/YPg4RPU.jpg")
t = 0

scene.autoscale = True
theta=2*3.14159/24 
EarthToSun = 50
MoonToEarth = 2
while True:
    rate(10)
    earth.pos.x = EarthToSun*cos(t)
    earth.pos.z = EarthToSun*sin(t)
    moon.pos.x = earth.pos.x+MoonToEarth*cos(10*t)
    moon.pos.z = earth.pos.z+MoonToEarth*sin(10*t)
    earth.rotate(angle=theta, axis=vector(0,1,0), origin=vector(0,0,0))
    moon.rotate(angle=theta, axis=vector(0,1,0), origin=vector(0,0,0))
    sun.rotate(angle=theta*0.2, axis=vector(0,1,0), origin=vector(0,0,0))
    t+=0.01
