from Tkinter import *
import numpy as np
import math
from scipy.optimize import leastsq



global h,w
h,w=0,0


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

window = np.zeros((9,2),float)


def choose_painting(event):
    global photo
    global item
    global w,h

    
    temp = var.get()
    if temp == "Music":
        photo = PhotoImage(file="xl_music.gif"); w = photo.width(); h = photo.height(); c.itemconfigure(item, image=photo)
            
    elif temp == "Officer":
        photo = PhotoImage(file="xl_officer.gif"); w = photo.width(); h = photo.height(); c.itemconfigure(item, image=photo)

    elif temp == "Art":
        photo = PhotoImage(file="xl_art.gif"); w = photo.width(); h = photo.height(); c.itemconfigure(item, image=photo)

    elif temp == "Astronomer":
        photo = PhotoImage(file="xl_astronomer.gif"); w = photo.width(); h = photo.height(); c.itemconfigure(item, image=photo)
        
    elif temp == "Beit":
        photo = PhotoImage(file="xl_beit.gif"); w = photo.width(); h = photo.height(); c.itemconfigure(item, image=photo)
        
    elif temp == "Concert":
        photo = PhotoImage(file="xl_concert.gif"); w = photo.width(); h = photo.height(); c.itemconfigure(item, image=photo)

    elif temp == "Faith":
        photo = PhotoImage(file="xl_faith.gif"); w = photo.width(); h = photo.height(); c.itemconfigure(item, image=photo)

    elif temp == "Geographer":
        photo = PhotoImage(file="xl_geographer.gif"); w = photo.width(); h = photo.height(); c.itemconfigure(item, image=photo)

    elif temp == "Berlin":
        photo = PhotoImage(file="xl_glass_berlin.gif"); w = photo.width(); h = photo.height(); c.itemconfigure(item, image=photo)
        
    elif temp == "Glass":
        photo = PhotoImage(file="xl_glass.gif"); w = photo.width(); h = photo.height(); c.itemconfigure(item, image=photo)
        
    elif temp == "Love":
        photo = PhotoImage(file="xl_love.gif"); w = photo.width(); h = photo.height(); c.itemconfigure(item, image=photo)

    elif temp == "Standing":
        photo = PhotoImage(file="xl_standinga.gif"); w = photo.width(); h = photo.height(); c.itemconfigure(item, image=photo)

    elif temp == "Canaletto":
        photo = PhotoImage(file="westminister.gif"); w = photo.width(); h = photo.height(); c.itemconfigure(item, image=photo)

    elif temp == "Milkmaid":
        photo = PhotoImage(file="xl_milk.gif"); w = photo.width(); h = photo.height(); c.itemconfigure(item, image=photo)

    elif temp == "Letter":
        photo = PhotoImage(file="xl_open.gif"); w = photo.width(); h = photo.height(); c.itemconfigure(item, image=photo)


def makeWindow():
    global grid
    p = np.zeros((9,3),float)
    p = 100.*grid
    
    moveX=moveY=0
    newScale=100
    moveZ=1
        
    # translate
    for i in range(0,9):
        p[i][0] += moveX
        p[i][1] += moveY
        p[i][2] += moveZ

    # project in X,Y & make window
    print p
    newwindow=[]
    for i in (1,2,5,3,6,7,1,0,3,5,8,7):
        X = (p[i][0]*newScale)/p[i][2] + (w/2)
        Y = (p[i][1]*newScale)/p[i][2] + (h/2)
        newwindow.extend([X,Y])
    
    return newwindow
    

def newWindow():
    global grid
    p = np.zeros((9,3),float)
    p = 100.*grid
    global moveZ
    global window
    moveX = x.get(); moveY = y.get(); moveZ = z.get(); rotX = x2.get(); rotY = y2.get(); rotZ = z2.get(); newScale=scale.get()
    

    # rotate x,y,z

    rotXcos = math.cos(math.radians(rotX))
    rotXsin = math.sin(math.radians(rotX))
    rotYcos = math.cos(math.radians(rotY))
    rotYsin = math.sin(math.radians(rotY))
    rotZcos = math.cos(math.radians(rotZ))
    rotZsin = math.sin(math.radians(rotZ))

    ##Rotation along X:
    for i in range(0,9):
        ty = p[i][1]
        tz = p[i][2]
        p[i][1] = ty*rotXcos + tz*rotXsin
        p[i][2] = tz*rotXcos - ty*rotXsin
    
    ##Rotation along Y:

    for i in range(0,9):
        tx = p[i][0]
        tz = p[i][2]
        p[i][0] = tx*rotYcos - tz*rotYsin
        p[i][2] = tz*rotYcos + tx*rotYsin


    ##Rotation along Z:

    for i in range(0,9):
        tx = p[i][0]
        ty = p[i][1]
        p[i][0] = tx*rotZcos + ty*rotZsin
        p[i][1] = ty*rotZcos - tx*rotZsin 
        
    # translate x,y,z
    for i in range(0,9):
        p[i][0] += moveX
        p[i][1] += moveY
        p[i][2] += moveZ

    # project in X,Y & make window

    newwindow=[]
    for i in (1,2,5,3,6,7,1,0,3,5,8,7):
        X = p[i][0]*newScale/p[i][2] + (w/2)
        Y = p[i][1]*newScale/p[i][2] + (h/2)
        window[i][0] = X
        window[i][1] = Y
        newwindow.extend([X,Y])

    
    # update on canvas

    c.coords(item2,*newwindow)



def moveInZ(event):
    global moveZ
    newScale = scale.get()
    temp = abs(moveZ)
    moveZ=z.get()
    if (abs(moveZ)>temp):
        newScale = newScale + (abs(moveZ)-temp)
    elif (abs(moveZ)<temp):
        newScale = newScale - (temp-abs(moveZ))
    scale.set(newScale)
    newWindow()

def moveInY(event):
    newWindow()

def moveInX(event):
    newWindow()


def changeScale(event):
    newWindow()

    
def rotate(event):
    newWindow()

def reset_values():
    x.set(0); y.set(0); z.set(100); x2.set(0); y2.set(0); z2.set(0); scale.set(100)
    newWindow()

def floor():
    global moveX,moveY,moveZ,rotX,rotY,rotZ,newScale
    temp = var.get()

    if temp == "Music":
        x.set(-198); y.set(317); z.set(890); x2.set(-90); y2.set(-48); z2.set(1); scale.set(809)

    elif temp == "Canaletto":   
        x.set(-445); y.set(-146); z.set(1560); x2.set(0); y2.set(90); z2.set(0); scale.set(1825)

    elif temp == "Art":
        x.set(253); y.set(420); z.set(850); x2.set(-68); y2.set(-46); z2.set(17); scale.set(706)
        
    elif temp == "Beit":
        x.set(-35); y.set(318); z.set(1540); x2.set(88); y2.set(35); z2.set(4); scale.set(1700)
        
    elif temp == "Concert":
        x.set(199); y.set(268); z.set(1260); x2.set(87); y2.set(57); z2.set(-1); scale.set(1262)

    elif temp == "Faith":
        x.set(-216); y.set(634); z.set(4010); x2.set(86); y2.set(52); z2.set(3); scale.set(2000)

    elif temp == "Berlin":
        x.set(-382); y.set(576); z.set(1350); x2.set(-90); y2.set(-36); z2.set(-5); scale.set(688)
        
    elif temp == "Glass":
        x.set(-401); y.set(651); z.set(1890); x2.set(87); y2.set(55); z2.set(-1); scale.set(990)
        
    elif temp == "Love":
        x.set(4); y.set(302); z.set(1330); x2.set(90); y2.set(37); z2.set(2); scale.set(1286)

    elif temp == "Standing":
        x.set(-235); y.set(424); z.set(2000); x2.set(-90); y2.set(44); z2.set(0); scale.set(1752)

    newWindow()

def wall():
    global moveX,moveY,moveZ,rotX,rotY,rotZ,newScale
    temp = var.get()

    if temp == "Music":
        x.set(-804); y.set(-1000); z.set(4690); x2.set(90); y2.set(-1); z2.set(88); scale.set(1311)
    
    elif temp == "Officer":
        x.set(-454); y.set(-47); z.set(1550); x2.set(89); y2.set(-1); z2.set(-89); scale.set(1014)

    elif temp == "Canaletto":
        x.set(-445); y.set(-146); z.set(1560); x2.set(0); y2.set(90); z2.set(0); scale.set(1825)

    elif temp == "Astronomer":
        x.set(-650); y.set(-176); z.set(2710); x2.set(88); y2.set(0); z2.set(90); scale.set(1515)

    elif temp == "Geographer":
        x.set(-575); y.set(-106); z.set(1780); x2.set(90); y2.set(-1); z2.set(90); scale.set(1078)

    elif temp == "Standing":
        x.set(-1000); y.set(13); z.set(5000); x2.set(90); y2.set(1); z2.set(90); scale.set(1773)

    elif temp == "Milkmaid":
        x.set(-537); y.set(-397); z.set(2290); x2.set(87); y2.set(0); z2.set(88); scale.set(1574)

    elif temp == "Letter":
        x.set(-265); y.set(8); z.set(2970); x2.set(1); y2.set(51); z2.set(1); scale.set(2000)



    newWindow()


def press(event):
    global window
    X = event.x
    Y = event.y
    global corner

    for i in range(0,9):
        if ((X < window[i][0]+10) and (X > window[i][0]-10) and (Y < window[i][1]+10) and (Y > window[i][1]-10)):
            corner = i

def motion(event):
    global window, corner
    window[corner][0] = event.x
    window[corner][1] = event.y
    newwindow=[]
    for i in (1,2,5,3,6,7,1,0,3,5,8,7):

        newwindow.extend([window[i][0],window[i][1]])
    # update on canvas

    c.coords(item2,*newwindow)


def residual(slides):
    global xpix, ypix
    x.set(slides[0])
    y.set(slides[1])
    z.set(slides[2])
    x2.set(slides[3])
    y2.set(slides[4])
    z2.set(slides[5])
    scale.set(slides[6])
    newWindow()
    print xpix - window[:,0]
    print ypix - window[:,1]
    res = np.concatenate((xpix - window[:,0],ypix - window[:,1]))
    return res


def calculate():
    global xpix, ypix, window
    print "to do"
    xpix = 1.*window[:,0]
    ypix = 1.*window[:,1]
    slides = 7*[0]
    slides[0] = x.get()
    slides[1] = y.get()
    slides[2] = z.get()
    slides[3] = x2.get()
    slides[4] = y2.get()
    slides[5] = z2.get()
    slides[6] = scale.get()
    leastsq(residual,slides)


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
c.bind("<Button-1>", press)
c.bind("<B1-Motion>", motion)

item2 = c.create_line(makeWindow(),fill="red")


OptionMenu(root, var, "Music","Officer","Canaletto","Art","Astronomer","Beit","Concert","Faith","Geographer","Berlin","Glass","Love","Standing","Milkmaid","Letter", command=choose_painting).pack()
Button(root, text='Reset', command=reset_values).pack()
Button(root, text='Floor', command=floor).pack()
Button(root, text='Window', command=wall).pack()
Button(root, text='Calculate', command=calculate).pack()


Scale(root, from_=-90, to=90, length=650, orient=VERTICAL, variable=z2, command=rotate).pack(side='right',padx=5)


Scale(root, from_=-90, to=90, length=650, orient=VERTICAL, variable=y2, command=rotate).pack(side='right',padx=5)


Scale(root, from_=-90, to=90, length=650, orient=VERTICAL, variable=x2, command=rotate).pack(side='right',padx=5)


Scale(root, from_=1, to=2000, length=650, orient=VERTICAL, variable=scale, command=changeScale).pack(side='right',padx=20)
scale.set(100)



Scale(root, from_=1, to=8000, length=650, orient=VERTICAL, variable=z, command=moveInZ).pack(side='right',padx=5)
z.set(100)


Scale(root, from_=-1000, to=1000, length=650, orient=VERTICAL, variable=y, command=moveInY).pack(side='right',padx=5)


Scale(root, from_=-1000, to=1000, length=650, orient=VERTICAL, variable=x, command=moveInX).pack(side='right',padx=5)

root.mainloop()


