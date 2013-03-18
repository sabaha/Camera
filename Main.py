from Tkinter import *
from PIL import Image, ImageTk
import numpy as np
import math




global h,w
h=w=0


imageFile = "xl_music.jpg"


grid = np.zeros((9,3),float)
grid[0] = [-1,1,0]
grid[1] = [0,1,0]
grid[2] = [1,1,0]
grid[3] = [-1,0,0]
grid[4] = [0,0,0]
grid[5] = [1,0,0]
grid[6] = [-1,-1,0]
grid[7] = [0,-1,0]
grid[8] = [1,-1,0]

print grid

def choose_painting(event):
    global photo
    global item

    temp = var.get()
    if temp == "Music":
        
        photo = ImageTk.PhotoImage(Image.open("xl_music.jpg"))
        w = photo.width()
        h = photo.height()
        c.itemconfigure(item, image=photo)
            
    elif temp == "Officer":
           
        photo = ImageTk.PhotoImage(Image.open("xl_officer.jpg"))
        w = photo.width()
        h = photo.height()
        c.itemconfigure(item, image=photo)


def makeWindow():
    global grid
    p = np.zeros((9,3),float)
    p = 1.*grid
    
    global moveX,moveY,moveZ,rotX,rotY,rotZ,newScale,w,h
    moveX=moveY=rotX=rotY=rotZ=0
    newScale=100
    moveZ=1
    
##    # scale grid
##    for i in range(0,9):
##        for j in range (0,2):
##            p[i][j]=grid[i][j]*newScale*10
    
    # translate x,y,z
    #X
    for i in range(0,9):    
        p[i][0]=p[i][0]+moveX

    #Y
    for i in range(0,9):    
        p[i][1]=p[i][1]+moveY

    #Z
    for i in range(0,9):
        p[i][2]=p[i][2]+moveZ

    # project in X,Y & make window
    print p
    window=[]
    for i in (1,2,5,3,6,7,1,0,3,5,8,7):
##        X = p[i][0]*(0.9*p[i][2])/p[i][2]
##        Y = p[i][1]*(0.9*p[i][2])/p[i][2]
        X = (p[i][0]*newScale)/p[i][2] + (w/2)
        print X
        
        Y = (p[i][1]*newScale)/p[i][2] + (h/2)
        print Y
        window.extend([X,Y])
    
    return window
    

def newWindow():
    global grid
    p = np.zeros((9,3),float)
    p = 1.*grid

    global moveX,moveY,moveZ,rotX,rotY,rotZ,newScale,w,h
    
##    # scale grid
##    for i in range(0,9):
##        for j in range (0,2):
##            p[i][j]=grid[i][j]*newScale*10

    # rotate x,y,z

    ##Rotation along X:
    ##y' = y*cos(a) + z*sin(a)
    ##z' = - y*sin(a) + z*cos(a)
    ##x' = x
    for i in range(0,9):
        y = p[i][1]
        z = p[i][2]
        p[i][1] = (y*math.cos(math.radians(rotX)) + z*math.sin(math.radians(rotX)))
        p[i][2] = (z*math.cos(math.radians(rotX)) - y*math.sin(math.radians(rotX)))
    
    ##Rotation along Y:
    ##z' = z*cos(a) + x*sin(a)
    ##x' = -z*sin(a) + x*cos(a)
    ##y' = y
    for i in range(0,9):
        x = p[i][0]
        z = p[i][2]
        p[i][0] = (x*math.cos(math.radians(rotY)) - z*math.sin(math.radians(rotY)))
        p[i][2] = (z*math.cos(math.radians(rotY)) + x*math.sin(math.radians(rotY)))


    ##Rotation along Z:
    ##x' = x*cos(a) + y*sin(a)
    ##y' = -x*sin(a) + y*cos(a)
    ##z' = z
    for i in range(0,9):
        x = p[i][0]
        y = p[i][1]
        p[i][0] = (x*math.cos(math.radians(rotZ)) + y*math.sin(math.radians(rotZ)))
        p[i][1] = (y*math.cos(math.radians(rotZ)) - x*math.sin(math.radians(rotZ)))
        
    # translate x,y,z
    #X
    for i in range(0,9):    
        p[i][0]=p[i][0]+moveX

    #Y
    for i in range(0,9):    
        p[i][1]=p[i][1]+moveY

    #Z
    for i in range(0,9):
        p[i][2]=p[i][2]+moveZ

    # project in X,Y & make window
    print "before perspective"
    print p
    newwindow=[]
    for i in (1,2,5,3,6,7,1,0,3,5,8,7):
##        X = p[i][0]*(0.9*p[i][2])/p[i][2]
##        Y = p[i][1]*(0.9*p[i][2])/p[i][2]
        X = (p[i][0]*newScale)/p[i][2] + (w/2)
        
        Y = (p[i][1]*newScale)/p[i][2] + (h/2)
        newwindow.extend([X,Y])
    print "after perspective"
    print newwindow
    
    # update on canvas

    c.coords(item2,*newwindow)



def moveInZ(event):
    global moveZ
    moveZ=z.get()    
    newWindow()

def moveInY(event):
    global moveY
    moveY=y.get()    
    newWindow()

def moveInX(event):
    global moveX
    moveX=x.get()    
    newWindow()


def changeScale(event):
    global newScale
    newScale=scale.get()
    newWindow()


##Rotation along Z:
##x' = x*cos(a) + y*sin(a)
##y' = -x*sin(a) + y*cos(a)
##z' = z
    
def rotateInZ(event):
    global rotZ
    rotZ = z2.get()
    newWindow()


##Rotation along Y:
##z' = z*cos(a) + x*sin(a)
##x' = -z*sin(a) + x*cos(a)
##y' = y
##

def rotateInY(event):
    global rotY
    rotY = y2.get()
    newWindow()
    
##Rotation along X:
##y' = y*cos(a) + z*sin(a)
##z' = - y*sin(a) + z*cos(a)
##x' = x
##
def rotateInX(event):
    global rotX
    rotX = x2.get()
    newWindow()
    

def reset_values():
    print "comes in there"
    global moveX,moveY,moveZ,rotX,rotY,rotZ,newScale
    moveX=moveY=rotX=rotY=rotZ=0
    moveZ=1
    newScale=100
    x.set(0)
    y.set(0)
    z.set(1)
    x2.set(0)
    y2.set(0)
    z2.set(0)
    scale.set(100)
    print "makes it to here"
    newWindow()


root = Tk()
var = StringVar()
var.set("Music")


x,y,z,scale,x2,y2,z2=DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar()
    




image1 = ImageTk.PhotoImage(Image.open(imageFile))
w = image1.width()
h = image1.height()


c = Canvas(root, width=w,height=h)
c.pack(side='left',fill='both',expand='yes')
item = c.create_image(0, 0, anchor=NW, image=image1)
c.image = image1

window=[]
window=makeWindow()

item2 = c.create_line(window,fill="red")


OptionMenu(root, var, "Music","Officer", command=choose_painting).pack()
Button(root, text='Reset', command=reset_values).pack()


Scale(root, from_=-90, to=90, length=600, orient=VERTICAL, variable=z2, command=rotateInZ).pack(side='right',padx=5)
##scale2.set(0)
##scale2.pack(side='right',padx=5)
##scale2.bind('<ButtonRelease>', rotateInZ)

Scale(root, from_=-90, to=90, length=600, orient=VERTICAL, variable=y2, command=rotateInY).pack(side='right',padx=5)
#scale3.set(0)
#scale3.pack(side='right',padx=5)
#scale3.bind('<ButtonRelease>', rotateInY)

Scale(root, from_=-90, to=90, length=600, orient=VERTICAL, variable=x2, command=rotateInX).pack(side='right',padx=5)
#scale4.set(0)
#scale4.pack(side='right',padx=5)
#scale4.bind('<ButtonRelease>', rotateInX)

Scale(root, from_=1, to=1000, length=600, orient=VERTICAL, variable=scale, command=changeScale ).pack(side='right',padx=20)
scale.set(100)
##scale.pack(side='right',padx=20)
##scale.bind('<ButtonRelease>', changeScale)



Scale(root, from_=-100, to=100, length=600, orient=VERTICAL, variable=z, command=moveInZ).pack(side='right',padx=5)
z.set(1)
##z.pack(side='right',padx=5)
##z.bind('<ButtonRelease>', moveInZ)

Scale(root, from_=-30, to=30, length=600, orient=VERTICAL, variable=y, command=moveInY).pack(side='right',padx=5)
##y.set(0)
##y.pack(side='right',padx=5)
##y.bind('<ButtonRelease>', moveInY)

Scale(root, from_=-30, to=30, length=600, orient=VERTICAL, variable=x, command=moveInX).pack(side='right',padx=5)
##x.set(0)
##x.pack(side='right',padx=5)
##x.bind('<ButtonRelease>', moveInX)



root.mainloop()


