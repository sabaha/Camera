from Tkinter import *
import numpy as np
import math




global h,w
h=w=0


imageFile = "xl_music.gif"


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
        
        photo = PhotoImage(file="xl_music.gif")
        w = photo.width()
        h = photo.height()
        c.itemconfigure(item, image=photo)
            
    elif temp == "Officer":
           
        photo = PhotoImage(file="xl_officer.gif")
        w = photo.width()
        h = photo.height()
        c.itemconfigure(item, image=photo)

    elif temp == "Art":
           
        photo = PhotoImage(file="xl_art.gif")
        w = photo.width()
        h = photo.height()
        c.itemconfigure(item, image=photo)

    elif temp == "Astronomer":
           
        photo = PhotoImage(file="xl_astronomer.gif")
        w = photo.width()
        h = photo.height()
        c.itemconfigure(item, image=photo)
        
    elif temp == "Beit":
           
        photo = PhotoImage(file="xl_beit.gif")
        w = photo.width()
        h = photo.height()
        c.itemconfigure(item, image=photo)
        
    elif temp == "Concert":
           
        photo = PhotoImage(file="xl_concert.gif")
        w = photo.width()
        h = photo.height()
        c.itemconfigure(item, image=photo)

    elif temp == "Faith":
           
        photo = PhotoImage(file="xl_faith.gif")
        w = photo.width()
        h = photo.height()
        c.itemconfigure(item, image=photo)

    elif temp == "Geographer":
           
        photo = PhotoImage(file="xl_geographer.gif")
        w = photo.width()
        h = photo.height()
        c.itemconfigure(item, image=photo)

    elif temp == "Berlin":
           
        photo = PhotoImage(file="xl_glass_berlin.gif")
        w = photo.width()
        h = photo.height()
        c.itemconfigure(item, image=photo)
        
    elif temp == "Glass":
           
        photo = PhotoImage(file="xl_glass.gif")
        w = photo.width()
        h = photo.height()
        c.itemconfigure(item, image=photo)
        
    elif temp == "Love":
           
        photo = PhotoImage(file="xl_love.gif")
        w = photo.width()
        h = photo.height()
        c.itemconfigure(item, image=photo)

    elif temp == "Standing":
           
        photo = PhotoImage(file="xl_standinga.gif")
        w = photo.width()
        h = photo.height()
        c.itemconfigure(item, image=photo)

    elif temp == "Canaletto":
           
        photo = PhotoImage(file="westminister.gif")
        w = photo.width()
        h = photo.height()
        c.itemconfigure(item, image=photo)

def makeWindow():
    global grid
    p = np.zeros((9,3),float)
    p = 10.*grid
    
    global moveX,moveY,moveZ,rotX,rotY,rotZ,newScale,w,h
    moveX=moveY=rotX=rotY=rotZ=0
    newScale=100
    moveZ=1
    
    
    # translate
    for i in range(0,9):
        p[i][0] += 0.1*moveX
        p[i][1] += 0.1*moveY
        p[i][2] += moveZ

    # project in X,Y & make window
    print p
    window=[]
    for i in (1,2,5,3,6,7,1,0,3,5,8,7):

        X = (p[i][0]*newScale)/p[i][2] + (w/2)
        print X
        
        Y = (p[i][1]*newScale)/p[i][2] + (h/2)
        print Y
        window.extend([X,Y])
    
    return window
    

def newWindow():
    global grid
    p = np.zeros((9,3),float)
    p = 10.*grid

    global moveX,moveY,moveZ,rotX,rotY,rotZ,newScale,w,h
    
## # scale grid
## for i in range(0,9):
## for j in range (0,2):
## p[i][j]=grid[i][j]*newScale*10

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
    for i in range(0,9):
        p[i][0] += 0.1*moveX
        p[i][1] += 0.1*moveY
        p[i][2] += moveZ

    # project in X,Y & make window
## print "before perspective"
## print p
    newwindow=[]
    for i in (1,2,5,3,6,7,1,0,3,5,8,7):
## X = p[i][0]*(0.9*p[i][2])/p[i][2]
## Y = p[i][1]*(0.9*p[i][2])/p[i][2]
        X = (p[i][0]*newScale)/p[i][2] + (w/2)
        
        Y = (p[i][1]*newScale)/p[i][2] + (h/2)
        newwindow.extend([X,Y])
## print "after perspective"
## print newwindow
    
    # update on canvas

    c.coords(item2,*newwindow)



def moveInZ(event):
    global moveZ, newScale
    temp = abs(moveZ)
    moveZ=z.get()
    if (abs(moveZ)>temp):
        newScale = newScale + 10*(abs(moveZ)-temp)
    elif (abs(moveZ)<temp):
        newScale = newScale - 10*(temp-abs(moveZ))
    scale.set(newScale)
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

    global moveX,moveY,moveZ,rotX,rotY,rotZ,newScale
    moveX,moveY,rotX,rotY,rotZ=0,0,0,0,0
    moveZ=1
    newScale=100
    x.set(0)
    y.set(0)
    z.set(1)
    x2.set(0)
    y2.set(0)
    z2.set(0)
    scale.set(100)

    newWindow()

def floor():
    global moveX,moveY,moveZ,rotX,rotY,rotZ,newScale
    temp = var.get()

    if temp == "Music":

        x.set(-123)
        y.set(320)
        z.set(173)
        x2.set(78)
        y2.set(43)
        z2.set(6)
        scale.set(1447)
        moveX = x.get()
        moveY = y.get()
        moveZ = z.get()
        rotX = x2.get()
        rotY = y2.get()
        rotZ = z2.get()
        newScale=scale.get()
    

    elif temp == "Canaletto":
           
        x.set(-445)
        y.set(-146)
        z.set(156)
        x2.set(0)
        y2.set(90)
        z2.set(0)
        scale.set(1825)
        moveX = x.get()
        moveY = y.get()
        moveZ = z.get()
        rotX = x2.get()
        rotY = y2.get()
        rotZ = z2.get()
        newScale=scale.get()

    elif temp == "Art":
           
        x.set(35)
        y.set(496)
        z.set(135)
        x2.set(-80)
        y2.set(-39)
        z2.set(5)
        scale.set(972)
        moveX = x.get()
        moveY = y.get()
        moveZ = z.get()
        rotX = x2.get()
        rotY = y2.get()
        rotZ = z2.get()
        newScale=scale.get()

        
    elif temp == "Beit":
           
        x.set(-18)
        y.set(356)
        z.set(173)
        x2.set(90)
        y2.set(39)
        z2.set(0)
        scale.set(1652)
        moveX = x.get()
        moveY = y.get()
        moveZ = z.get()
        rotX = x2.get()
        rotY = y2.get()
        rotZ = z2.get()
        newScale=scale.get()
        
    elif temp == "Concert":
           
        x.set(229)
        y.set(229)
        z.set(114)
        x2.set(88)
        y2.set(55)
        z2.set(-1)
        scale.set(1074)
        moveX = x.get()
        moveY = y.get()
        moveZ = z.get()
        rotX = x2.get()
        rotY = y2.get()
        rotZ = z2.get()
        newScale=scale.get()

    elif temp == "Faith":
           
        x.set(-445)
        y.set(-146)
        z.set(156)
        x2.set(0)
        y2.set(90)
        z2.set(0)
        scale.set(1825)
        moveX = x.get()
        moveY = y.get()
        moveZ = z.get()
        rotX = x2.get()
        rotY = y2.get()
        rotZ = z2.get()
        newScale=scale.get()


    elif temp == "Berlin":
           
        x.set(349)
        y.set(363)
        z.set(87)
        x2.set(86)
        y2.set(-53)
        z2.set(0)
        scale.set(427)
        moveX = x.get()
        moveY = y.get()
        moveZ = z.get()
        rotX = x2.get()
        rotY = y2.get()
        rotZ = z2.get()
        newScale=scale.get()
        
    elif temp == "Glass":
           
        x.set(-413)
        y.set(698)
        z.set(200)
        x2.set(90)
        y2.set(52)
        z2.set(-1)
        scale.set(1023)
        moveX = x.get()
        moveY = y.get()
        moveZ = z.get()
        rotX = x2.get()
        rotY = y2.get()
        rotZ = z2.get()
        newScale=scale.get()
        
    elif temp == "Love":
           
        x.set(4)
        y.set(310)
        z.set(133)
        x2.set(90)
        y2.set(41)
        z2.set(0)
        scale.set(1275)
        moveX = x.get()
        moveY = y.get()
        moveZ = z.get()
        rotX = x2.get()
        rotY = y2.get()
        rotZ = z2.get()
        newScale=scale.get()

    elif temp == "Standing":
           
        x.set(-231)
        y.set(413)
        z.set(228)
        x2.set(90)
        y2.set(943)
        z2.set(0)
        scale.set(2000)
        moveX = x.get()
        moveY = y.get()
        moveZ = z.get()
        rotX = x2.get()
        rotY = y2.get()
        rotZ = z2.get()
        newScale=scale.get()

    newWindow()

def wall():
    global moveX,moveY,moveZ,rotX,rotY,rotZ,newScale
    temp = var.get()

    if temp == "Music":

        x.set(-515)
        y.set(-708)
        z.set(300)
        x2.set(0)
        y2.set(90)
        z2.set(0)
        scale.set(1292)
        moveX = x.get()
        moveY = y.get()
        moveZ = z.get()
        rotX = x2.get()
        rotY = y2.get()
        rotZ = z2.get()
        newScale=scale.get()
    
    elif temp == "Officer":
           
        x.set(-452)
        y.set(-182)
        z.set(171)
        x2.set(1)
        y2.set(90)
        z2.set(0)
        scale.set(1127)
        moveX = x.get()
        moveY = y.get()
        moveZ = z.get()
        rotX = x2.get()
        rotY = y2.get()
        rotZ = z2.get()
        newScale=scale.get()

    elif temp == "Canaletto":
           
        x.set(-445)
        y.set(-146)
        z.set(156)
        x2.set(0)
        y2.set(90)
        z2.set(0)
        scale.set(1825)
        moveX = x.get()
        moveY = y.get()
        moveZ = z.get()
        rotX = x2.get()
        rotY = y2.get()
        rotZ = z2.get()
        newScale=scale.get()


    elif temp == "Astronomer":
           
        x.set(-641)
        y.set(-162)
        z.set(246)
        x2.set(-1)
        y2.set(90)
        z2.set(0)
        scale.set(1388)
        moveX = x.get()
        moveY = y.get()
        moveZ = z.get()
        rotX = x2.get()
        rotY = y2.get()
        rotZ = z2.get()
        newScale=scale.get()
        

    elif temp == "Geographer":
           
        x.set(-482)
        y.set(-113)
        z.set(168)
        x2.set(-1)
        y2.set(90)
        z2.set(3)
        scale.set(821)
        moveX = x.get()
        moveY = y.get()
        moveZ = z.get()
        rotX = x2.get()
        rotY = y2.get()
        rotZ = z2.get()
        newScale=scale.get()

    elif temp == "Berlin":
           
        x.set(-445)
        y.set(-146)
        z.set(156)
        x2.set(0)
        y2.set(90)
        z2.set(0)
        scale.set(1825)
        moveX = x.get()
        moveY = y.get()
        moveZ = z.get()
        rotX = x2.get()
        rotY = y2.get()
        rotZ = z2.get()
        newScale=scale.get()
        
##    elif temp == "Glass":
##           
##        x.set(-445)
##        y.set(-146)
##        z.set(156)
##        x2.set(0)
##        y2.set(90)
##        z2.set(0)
##        scale.set(1825)
##        moveX = x.get()
##        moveY = y.get()
##        moveZ = z.get()
##        rotX = x2.get()
##        rotY = y2.get()
##        rotZ = z2.get()
##        newScale=scale.get()
        

    elif temp == "Standing":
           
        x.set(-445)
        y.set(-146)
        z.set(156)
        x2.set(0)
        y2.set(90)
        z2.set(0)
        scale.set(1825)
        moveX = x.get()
        moveY = y.get()
        moveZ = z.get()
        rotX = x2.get()
        rotY = y2.get()
        rotZ = z2.get()
        newScale=scale.get()


    newWindow()

    

root = Tk()
var = StringVar()
var.set("Music")


x,y,z,scale,x2,y2,z2=DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar()
    




image1 = PhotoImage(file=imageFile)
w = image1.width()
h = image1.height()


c = Canvas(root, width=w,height=h)
c.pack(side='left',fill='both',expand='yes')
item = c.create_image(0, 0, anchor=NW, image=image1)
c.image = image1

window=[]
window=makeWindow()

item2 = c.create_line(window,fill="red")


OptionMenu(root, var, "Music","Officer","Canaletto","Art","Astronomer","Beit","Concert","Faith","Geographer","Berlin","Glass","Love","Standing", command=choose_painting).pack()
Button(root, text='Reset', command=reset_values).pack()
Button(root, text='Floor', command=floor).pack()
Button(root, text='Window', command=wall).pack()


Scale(root, from_=-90, to=90, length=650, orient=VERTICAL, variable=z2, command=rotateInZ).pack(side='right',padx=5)


Scale(root, from_=-90, to=90, length=650, orient=VERTICAL, variable=y2, command=rotateInY).pack(side='right',padx=5)


Scale(root, from_=-90, to=90, length=650, orient=VERTICAL, variable=x2, command=rotateInX).pack(side='right',padx=5)


Scale(root, from_=1, to=2000, length=650, orient=VERTICAL, variable=scale, command=changeScale ).pack(side='right',padx=20)
scale.set(100)



Scale(root, from_=1, to=500, length=650, orient=VERTICAL, variable=z, command=moveInZ).pack(side='right',padx=5)
z.set(1)


Scale(root, from_=-1000, to=1000, length=650, orient=VERTICAL, variable=y, command=moveInY).pack(side='right',padx=5)


Scale(root, from_=-1000, to=1000, length=650, orient=VERTICAL, variable=x, command=moveInX).pack(side='right',padx=5)

root.mainloop()


