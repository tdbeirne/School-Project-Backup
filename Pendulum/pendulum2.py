#TODO: ACTUALLY SOLVE THE INTEGRAL, MAKE IT RUN SMOOTHER, LET THE USER INTERACT WITH PENDULUM IN REAL TIME


import math
import numpy as np
import time
from graphics import *
from scipy.integrate import odeint
import matplotlib.pyplot as plt

List1 = []
List2 = []
List3 = []
List4 = []

angList1 = []
angList2 = []

iList = []

#Set up variables that describe the pendulum:
#For some reason this thing just blows up if g gets too big. The bobs move too fast and it gets angry and the accels blow up. It starts to spin faster than light
#I think this happens because it doesn't actually solve the integral it just "adds areas"
#If we approximated better by integrating and solving this would probably be smoother
#Keep g equal to or below 6 and things should be okay
#Nah I just tested it and it can get pretty mad still
#I think if something exceeds a certain value it just throws up. Like if you cross a threshold which should be uncrossable it diverges
#If I actually solved the integral, crossing that threshold, no matter how slight, would have been impossible
g = 3.0
L1 = 100.0
L2 = 100.0
m1 = 10.0
m2 = 10.0

#set up angles
a1 = (np.pi*.3001)
a2 = (np.pi*.3002)
a1_v = 0.0
a2_v = 0.0
a1_a = 0.0
a2_a = 0.0

#set up graphics window
wwidth = 500
wheight = 500
win = GraphWin("Pendulum", wwidth, wheight, autoflush = False)


#set origin point and starting point for bobs
orig1 = int(wwidth/2)
orig2 = int(wheight/3)

x1 = orig1 + L1 * np.sin(a1)
y1 = orig2 + -L1 * np.cos(a1)
x2 = x1 + L2 * np.sin(a2)
y2 = y1 - L2 * np.cos(a2)

origpt = Point(orig1,orig2)
pt1 = Point(x1,y1)
pt2 = Point(x2,y2)


#draw shapes for pendulum
origCir = Circle(origpt, 25)
origCir.setFill('red')

cir1 = Circle(pt1, 25)
cir1.setFill('black')

cir2 = Circle(pt2, 25)
cir2.setFill('black')

lin1 = Line(origpt, pt1)
lin1.setWidth(5)

lin2 = Line(pt1, pt2)
lin2.setWidth(5)

origCir.draw(win)
cir1.draw(win)
cir2.draw(win)
lin1.draw(win)
lin2.draw(win)

#put shapes into a list for easy updating
pendShapes = [origCir,cir1,cir2,lin1,lin2]

#initialize numerator and denominator as floats
numerator1 = 0.0
denom1 = 0.0

numerator2 = 0.0
denom2 = 0.0


#calculate angular acceleration and update angular velocity and angle
def pend_step():
    global g
    global a1
    global a2
    global m1
    global m2
    global L1
    global L2
    global a1_v
    global a2_v
    global a1_a
    global a2_a
    global x1
    global x2
    global y1
    global y2
    #numerator and denominator of equation 1
    numerator1 = -g * (2 * m1 + m2) * np.sin(a1) - (m2 * g * np.sin(a1 - (2 * a2))) + (-2 * np.sin(a1 - a2) * m2 * ((np.power(a2_v,2) * L2) + (np.power(a1_v, 2) * L1 * np.cos(a1 - a2))))
    denom1 = L1 * ((2 * m1 + m2) - (m2 * np.cos(2 * a1 - 2 * a2)))

    #numerator and denominator of equation 2
    numerator2 = (2*np.sin(a1 - a2))*((np.power(a1_v, 2)*L1*(m1 + m2)) + (g*(m1 + m2)*np.cos(a1)) + (np.power(a2_v, 2) * L2 * m2 * np.cos(a1 - a2)))
    denom2 = L2 * ((2 * m1 + m2) - (m2 * np.cos(2 * a1 - 2 * a2)))

    #calculate angular acceleration
    a1_a = numerator1/denom1
    a2_a = numerator2/denom2

    #calculate velocity and current angle
    a1_v += a1_a
    a2_v += a2_a
    a1 += a1_v
    a2 += a2_v

    x1 = orig1 + L1 * np.sin(a1)
    y1 = orig2 + L1 * np.cos(a1)

    x2 = x1 + L2 * np.sin(a2)
    y2 = y1 + L2 * np.cos(a2)

    #a1 = a1 % (2 * np.pi)
    #a2 = a2 % (2 * np.pi)

    List1.append(a1_v)
    List2.append(a2_v)
    List3.append(((np.power(a2_v,2) * L2) + (np.power(a1_v, 2) * L1 * np.cos(a1 - a2))))

    angList1.append(a1)
    angList2.append(a2)

    print("a1_v")
    print(a1_v)
    #print("a2_v")
    #print(a2_v)
    #print("eq3")
    #print(((np.power(a2_v,2) * L2) + (np.power(a1_v, 2) * L1 * np.cos(a1 - a2))))

#draws the pendulum, window is the graphics window you want to display it on
def draw_pend(window):
    global pt1
    global pt2
    global x1
    global y1
    global x2
    global y2
    global origpt
    global cir1
    global cir2
    global lin1
    global lin2

    cir1.undraw()
    cir2.undraw()
    lin1.undraw()
    lin2.undraw()

    pt1 = Point(x1,y1)
    pt2 = Point(x2,y2)

    cir1 = Circle(pt1, 15)
    cir2 = Circle(pt2, 15)
    lin1 = Line(origpt, pt1)
    lin2 = Line(pt1, pt2)

    cir1.setFill('black')
    cir2.setFill('black')

    cir1.draw(window)
    cir2.draw(window)
    lin1.draw(window)
    lin2.draw(window)

    update()
    time.sleep(.05)

for i in range(1,360):
    print("iteration")
    print(i)
    pend_step()
    draw_pend(win)





#plt.figure(1)

#plt.subplot(231)
#plt.plot(List1)
#plt.plot(List3)
#plt.ylabel("a1_v + stuff")

#plt.subplot(232)
#plt.plot(List1)
#plt.ylabel("a1_v")

#plt.subplot(233)
#plt.plot(List3)
#plt.ylabel("eq3")

#plt.subplot(234)
#plt.plot(angList1)
#plt.ylabel("angle1")

#plt.subplot(235)
#plt.plot(angList2)
#plt.ylabel("angle2")




plt.plot(angList1)
plt.plot(angList2)
plt.ylabel("angles")

plt.show()
