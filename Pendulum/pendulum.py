import math
import numpy as np
import time
from graphics import *

#set graphics window dimensions
wwidth = 500
wheight = 500

#set origin point
orig1 = int(wwidth/2)
orig2 = int(wheight/3)

#set up pendulum specifics (radius, angle, mass etc.)
r1 = 100.0
r2 = 100.0

ang1 = 0.0
ang2 = 0.0

mass1 = 10.0
mass2 = 10.0

x1 = orig1 + r1 * math.cos(ang1)
y1 = orig2 + r1 * math.sin(ang1)

x2 = x1 + r2 * math.cos(ang2)
y2 = y1 + r2 * math.sin(ang2)




#creates the graphics window
win = GraphWin("Pendulum", wwidth, wheight, autoflush = False)


#set up graphics for pendulum
origpt = Point(orig1,orig2)
pt1 = Point(x1,y1)
pt2 = Point(x2,y2)


origCir = Circle(origpt, 45)
origCir.setFill('black')

cir1 = Circle(pt1, 25)
cir1.setFill('black')

cir2 = Circle(pt2, 25)
cir2.setFill('black')
#line1 = Line()

lin1 = Line(origpt, pt1)
lin1.setWidth(5)

lin2 = Line(pt1, pt2)
lin2.setWidth(5)


shapeList = [origCir,cir1,cir2,lin1,lin2]



def redrawAll(window, shapeList):
    ''' Move all shapes in shapeList by (dx, dy).'''
    for shape in shapeList:
        shape.undraw()
        shape.draw(window)
        update()


origCir.draw(win)
cir1.draw(win)
cir2.draw(win)
lin1.draw(win)
lin2.draw(win)
update()

time.sleep(10)
cir2.undraw()
update()




win.getMouse()
win.close()




def runge_kutta()
