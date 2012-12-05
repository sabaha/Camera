# -*- coding: utf-8 -*-

from Tkinter import *
from PIL import Image, ImageTk
import numpy as np
import math


p = np.zeros((9,3),float)
p[0] = [200,200,1]
p[1] = [300,200,1]
p[2] = [400,200,1]
p[3] = [200,300,1]
p[4] = [300,300,1]
p[5] = [400,300,1]
p[6] = [200,400,1]
p[7] = [300,400,1]
p[8] = [400,400,1]

##window=[]
##for i in range(0,9):
##    window.extend([p[i][0],p[i][1]])

##grid = zeros((9,3))
##grid[0] = [-1,1,0]
##grid[1] = [0,1,0]
##grid[2] = [1,1,0]
##grid[3] = [-1,0,0]
##grid[4] = [0,0,0]
##grid[5] = [1,0,0]
##grid[6] = [-1,-1,0]
##grid[7] = [0,-1,0]
##grid[8] = [1,-1,0]
##


window=[]
for i in (1,2,5,3,6,7,1,0,3,5,8,7):
    X = p[i][0]*(0.9*p[i][2])/p[i][2]
    Y = p[i][1]*(0.9*p[i][2])/p[i][2]
    window.extend([X,Y])

##window = [p[1][0],p[1][1],p[2][0],p[2][1],p[5][0],p[5][1],
##              p[3][0],p[3][1],p[6][0],p[6][1],p[7][0],p[7][1],
##              p[1][0],p[1][1],p[0][0],p[0][1],p[3][0],p[3][1],
##              p[5][0],p[5][1],p[8][0],p[8][1],p[7][0],p[7][1]]    

global oldZ,oldY,oldX,oldZr,oldYr,oldXr,oldCS
oldX=oldY=oldZ=oldZr=oldYr=oldXr= 0
oldCS = 100;

root = Tk()

imageFile = "xl_music.jpg"
image1 = ImageTk.PhotoImage(Image.open(imageFile))
# get the image size
w = image1.width()
h = image1.height()
# position coordinates of root 'upper left corner'
#x = 0
#y = 0



c = Canvas(root, width=w,height=h)
c.pack(side='left',fill='both',expand='yes')
#panel1 = tk.Label(root, image=image1)
#panel1.pack(side='top', fill='both', expand='yes')
# put a button on the image panel to test it
#button2 = tk.Button(panel1, text='button2')
#button2.pack(side='top')


def newWindow():
    global oldCS, oldZ,oldY,oldX
##    p = grid
####    if (oldXr!=0):
####
####    if (oldYr!=0):
####
####    if (oldZr!=0):
##    print p      
##    for i in range(0,9):
##        p[i][0]=p[i][0]*oldCS + 0.5*w + oldX
##        p[i][1]=p[i][1]*oldCS + 0.5*h + oldY
##        p[i][2]=p[i][1]*oldCS + oldZ
##        print p
    newwindow=[]
    for i in (1,2,5,3,6,7,1,0,3,5,8,7):
        X = p[i][0]*(0.9*p[i][2])/p[i][2]
        Y = p[i][1]*(0.9*p[i][2])/p[i][2]
        newwindow.extend([X,Y])
    
##    newwindow = [p[1][0],p[1][1],p[2][0],p[2][1],p[5][0],p[5][1],
##              p[3][0],p[3][1],p[6][0],p[6][1],p[7][0],p[7][1],
##              p[1][0],p[1][1],p[0][0],p[0][1],p[3][0],p[3][1],
##              p[5][0],p[5][1],p[8][0],p[8][1],p[7][0],p[7][1]]

##    newwindow=[]
##    for i in range(0,9):
##        window.extend([p[i][0],p[i][1]])
    c.coords(item,*newwindow)

def show_values():
    print (w2.get())

def moveInZ(event):
    global oldZ
    temp = z.get() - oldZ
    for i in range(0,9):
        p[i][2]=p[i][2]+temp
    oldZ=z.get()    
    newWindow()

def moveInY(event):
    global oldY
    temp = y.get() - oldY
    for i in range(0,9):    
        p[i][1]=p[i][1]+temp
    oldY=y.get()    
    newWindow()

def moveInX(event):
    global oldX
    temp = x.get() - oldX
    for i in range(0,9):    
        p[i][0]=p[i][0]+temp
    oldX=x.get()    
    newWindow()


def changeScale(event):
    global oldCS
    oldCS=scale.get()


##Rotation along Z:
##x' = x*cos(a) + y*sin(a)
##y' = -x*sin(a) + y*cos(a)
##z' = z
    
def rotateInZ(event):
    global oldZr
    temp = z2.get() - oldZr
    X = p[4][0]
    Y = p[4][1]
    for i in range(0,9):
        x = p[i][0] - X
        y = p[i][1] - Y
        p[i][0] = (x*math.cos(math.radians(temp)) + y*math.sin(math.radians(temp))) + X
        p[i][1] = (y*math.cos(math.radians(temp)) - x*math.sin(math.radians(temp))) + Y
        
    oldZr = z2.get()
    newWindow()


##Rotation along Y:
##z' = z*cos(a) + x*sin(a)
##x' = -z*sin(a) + x*cos(a)
##y' = y
##

def rotateInY(event):
    global oldYr
    temp = y2.get() - oldYr
    X = p[4][0]
    Z = p[4][2]
    for i in range(0,9):
        x = p[i][0] - X
        z = p[i][2] - Z
        p[i][0] = (x*math.cos(math.radians(temp)) - z*math.sin(math.radians(temp))) + X
        p[i][2] = (z*math.cos(math.radians(temp)) + x*math.sin(math.radians(temp))) + Z
    
    oldYr = y2.get()
    newWindow()
    
##Rotation along X:
##y' = y*cos(a) + z*sin(a)
##z' = - y*sin(a) + z*cos(a)
##x' = x
##
def rotateInX(event):
    global oldXr
    temp = x2.get() - oldXr
    Y = p[4][1]
    Z = p[4][2]
    for i in range(0,9):
        y = p[i][1] - Y
        z = p[i][2] - Z
        p[i][1] = (y*math.cos(math.radians(temp)) + z*math.sin(math.radians(temp))) + Y
        p[i][2] = (z*math.cos(math.radians(temp)) - y*math.sin(math.radians(temp))) + Z
    
    oldXr = x2.get()
    newWindow()
    


    
c.create_image(0, 0, anchor=NW, image=image1)


item = c.create_line(window)
#w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))



#w.create_polygon(xy,fill='white',outline='black')


# save the panel's image from 'garbage collection'
c.image = image1
# start the event loop

z2 = Scale(root, from_=-90, to=90, length=600, orient=VERTICAL)
z2.set(0)
z2.pack(side='right',padx=5)
z2.bind('<ButtonRelease>', rotateInZ)

y2 = Scale(root, from_=-90, to=90, length=600, orient=VERTICAL)
y2.set(0)
y2.pack(side='right',padx=5)
y2.bind('<ButtonRelease>', rotateInY)

x2 = Scale(root, from_=-90, to=90, length=600, orient=VERTICAL)
x2.set(0)
x2.pack(side='right',padx=5)
x2.bind('<ButtonRelease>', rotateInX)

scale = Scale(root, from_=1, to=200, length=600, orient=VERTICAL)
scale.set(100)
scale.pack(side='right',padx=20)
scale.bind('<ButtonRelease>', changeScale)



z = Scale(root, from_=-100, to=100, length=600, orient=VERTICAL)
z.set(0)
z.pack(side='right',padx=5)
z.bind('<ButtonRelease>', moveInZ)

y = Scale(root, from_=-100, to=100, length=600, orient=VERTICAL)
y.set(0)
y.pack(side='right',padx=5)
y.bind('<ButtonRelease>', moveInY)

x = Scale(root, from_=-100, to=100, length=600, orient=VERTICAL)
x.set(0)
x.pack(side='right',padx=5)
x.bind('<ButtonRelease>', moveInX)
#Button(root, text='Show', command=show_values).pack()

root.mainloop()
