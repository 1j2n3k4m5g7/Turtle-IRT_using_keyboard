# ------------------------------------------------------------------------------
# Real-Time Interactive Turtle
# © 2026 Jan Migo
#
# Licensed under PolyForm Noncommercial 1.0.0
# FULL LICENSE: See LICENSE file in project root.
#
# ADDITIONAL PERMISSION: Use in monetized online content (YouTube, Twitch, etc.) 
# is explicitly allowed. Commercial products require separate permission.
# ------------------------------------------------------------------------------


from turtle import *
from keyboard import *
from time import sleep as wait
import tkinter
import customlibs.save as save
import customlibs.converterPStoPNG as converterPStoPNG
import customlibs.codes as codes

working = True
tracer(0)
slow=False
fast=True
mov_speed=0.0
visible=True
pen_size=1
PD=False
PU=False
PL=False
PR=False
P_INSERT=False
Pf=False
Pfk=False
Pfe=False
Pfesc=False
Pfk=False
Pa=False
Pb=False
Pd=False
Pf7=False
f7_toggled=False
mainLoopWork=True
Pt=False
fillmode=False
Ptl=False
Ptr=False
tAngle=None
Pc=False
Pp=False
Po=False
Pl=False
Pn=False
Pe=False
PPU=False # page up
PPD=False # page down
P0=False
Pg=False
Pk=False
Ph=False
Pv=False
bgcol='white'
pencol='black'
fillcol='black'
turtleShape=False
chosenColor=None
chosenColor1=None
ps=1
colours=[
    "black",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "pink",
    "gray"
]
penup()

def wOP():
    wait(mov_speed)
    forward(1)
def sOP():
    wait(mov_speed)
    back(1)
def aOP():
    left(15)
def dOP():
    right(15)

pensize(pen_size)

while working:
    wait(0.005)
    update()
    if is_pressed('f7'):
        if Pf7==False:
            if f7_toggled:
                Pf7=True
                mainLoopWork=False
                f7_toggled=False
            else:
                Pf7=True
                mainLoopWork=True
                f7_toggled=True
      
    else:
        Pf7=False
    if mainLoopWork:
        # closing
        if is_pressed('x'):
            working=False
        # forward/back
        if is_pressed('w'):
            wOP()
        if is_pressed('s'):
            sOP()
        # turning
        if is_pressed('a'):
            if Pa==False:
                aOP()
                Pa=True
        else:
            Pa=False
        if is_pressed('d'):
            if Pd==False:
                dOP()
                Pd=True
        else:
            Pd=False
        if is_pressed('t'):
            if Pt==False:
                while Pt!=True:
                    update()
                    wait(0.005)
                    if is_pressed('l'):
                        if Ptl==False:
                            Pt=True
                            Ptl=True
                            Ptr=True
                            tAngle=numinput('Number entry', 'Enter turn angle:')
                            if tAngle!=None:
                                if tAngle<=360 and tAngle>=0-360:
                                    left(tAngle)
                                    tAngle=None
                    if is_pressed('r'):
                        if Ptr==False:
                            Pt=True
                            Ptl=True
                            Ptr=True
                            tAngle=numinput('Number entry', 'Enter turn angle:')
                            if tAngle!=None:
                                if tAngle<=360 and tAngle>=0-360:
                                    right(tAngle)
                                    tAngle=None
                    if is_pressed('esc'):
                        Pt=True
        else:
            Ptr=False
            Ptl=False
            Pt=False
        # pen up/down
        if is_pressed('down'):
            if PD==False:
                pendown()
                PD=True
        else:
            PD=False
        if is_pressed('up'):
            if PU==False:
                penup()
                PU=True
        else:
            PU=False
        # other
        if is_pressed('c'):
            if Pc==False:
                Pc=True
                promień=numinput("Circle", "Enter circle radius: ")
                if promień!=None:
                    circle(promień)
        else:
            Pc=False
        if is_pressed('p'):
            if Pp==False:
                Pp=True
                local_set_pensize=numinput("Pen size", "Enter pen size: ")
                if local_set_pensize!=None:
                    pen_size=local_set_pensize
                    ps=pen_size
                    pensize(ps)
        else:
            Pp=False
        if is_pressed('right'):
            if PR==False:
                PR=True
                ps=ps+1
                pensize(ps)
        else:
            PR=False
        if is_pressed('left'):
            if PL==False:
                PL=True
                ps=ps-1
                if ps>=1:
                    pensize(ps)
                else:
                    ps=1
                    pensize(ps)
        else:
            PL=False
        if is_pressed('0'):
            if P0==False:
                P0=True
                goto(0,0)
        else:
            P0=False
        if is_pressed('g'):
            if Pg==False:
                Pg=True
                gotoX=numinput("X", "Where you want to go (enter x)? ")
                gotoY=numinput("Y", "Where you want to go (enter y)? ")
                if gotoX!=None and gotoY!=None:
                    goto(gotoX,gotoY)
        else:
            Pg=False
        if is_pressed('k'):
            if Pk==False:
                Pk=True
                tkinter.messagebox.showinfo("Colors List", "Color codes:\n0 = white\n1 = black\n2 = red\n3 = orange\n4 = yellow\n5 = green\n6 = blue\n7 = violet\n8 = pink\n9 = gray")
                chosenColor = numinput("Pencolor", "Choose pen color (enter color code): ")
                if chosenColor!=None:
                    if chosenColor==0:
                        pencolor(254/255, 254/255, 254/255)
                        chosenColor=None
                    elif chosenColor>=1 and chosenColor<=9:
                        pencolor(colours[int(chosenColor-1)])
                        chosenColor=None
                    else:
                        tkinter.messagebox.showerror('Error', 'Wrong number value!')
        else:
            Pk=False
        if is_pressed('h'):
            if Ph==False:
                Ph=True
                if turtleShape==True:
                    turtleShape=False
                    shape('classic')
                else:
                    shape('turtle')
                    turtleShape=True
        else:
            Ph=False
        if is_pressed('v'):
            if Pv==False:
                Pv=True
                if visible:
                    visible=False
                    hideturtle()
                else:
                    visible=True
                    showturtle()
        else:
            Pv=False
        if is_pressed('insert'):
            if P_INSERT==False:
                P_INSERT=True
                inserted_KWRD=textinput("Code input page", "Input code here (type Help! for help): ")
                codes.init(inserted_KWRD)
        else:
            P_INSERT=False
        
        if is_pressed('b'):
            if Pb==False:
                Pb=True
                tkinter.messagebox.showinfo("Colors List", "Color codes:\n0 = white\n1 = black\n2 = red\n3 = orange\n4 = yellow\n5 = green\n6 = blue\n7 = violet\n8 = pink\n9 = gray")
                chosenColor = numinput("Background color", "Choose background color (enter color code): ")
                if chosenColor!=None:
                    if chosenColor==0:
                        Screen().bgcolor("white")
                        bgcol=[254/255,254/255,254/255]
                    elif chosenColor>=1 and chosenColor<=9:
                        Screen().bgcolor(colours[int(chosenColor-1)])
                        bgcol=colours[int(chosenColor-1)]
                        chosenColor=None
                    else:
                        tkinter.messagebox.showerror('Error', 'Wrong color value!')
        else:
            Pb=False
        
        if is_pressed('f'):
            if Pf==False:
               
                while Pf!=True:
                    if is_pressed('b'):
                        if Pfb==False:
                            Pf=True
                            Pfb=True
                            Pb=True
                            begin_fill()
                    if is_pressed('k'):
                        if Pfk==False:
                            Pf=True
                            Pfk=True
                            Pk=True
                            tkinter.messagebox.showinfo("Colors List", "Color codes:\n0 = white\n1 = black\n2 = red\n3 = orange\n4 = yellow\n5 = green\n6 = blue\n7 = violet\n8 = pink\n9 = gray")
                            chosenColor = numinput("Fill color", "Choose fill color (enter color code): ")
                            if chosenColor!=None:
                                if chosenColor==0:
                                    fillcolor(254/255,254/255,254/255)
                                elif chosenColor>=1 and chosenColor<=9:
                                    fillcolor(colours[int(chosenColor-1)])
                                    chosenColor=None
                                else:
                                    tkinter.messagebox.showerror('Error', 'Wrong color value!')
                    if is_pressed('e'):
                        if Pfe==False:
                            Pf=True
                            Pfe=True
                            end_fill()
                    if is_pressed('esc'):
                        if Pfesc==False:
                            Pf=True
                            Pfesc=True
        else:
            Pf=False
            Pfk=False
            Pfb=False
            Pfe=False
            Pfesc=False
        
        if is_pressed('n'):
            if Pn==False:
                Pn=True
                clear()
        else:
            Pn=False
        
        if is_pressed('o'):
            if Po==False:
                Po=True
                tkinter.messagebox.showinfo("Colors List", "Color codes:\n0 = white\n1 = black\n2 = red\n3 = orange\n4 = yellow\n5 = green\n6 = blue\n7 = violet\n8 = pink\n9 = gray")
                chosenColor = numinput("Pencolor", "Choose pen color (enter color code): ")
                chosenColor1 = numinput("Fill color", "Choose fill color (enter color code): ")
                if chosenColor1!=None and chosenColor!=None:
                    if chosenColor==0 and chosenColor1==0:
                        fillcolor(254/255, 254/255, 254/255)
                        pencolor(254/255, 254/255, 254/255)
                        chosenColor=None
                        chosenColor1=None
                    elif chosenColor==0 and chosenColor1>=1 and chosenColor1<=9:
                        pencolor(254/255,254/255,254/255)
                        fillcolor(colours[int(chosenColor1-1)])
                        chosenColor=None
                        chosenColor1=None
                    elif chosenColor>=1 and chosenColor<=9 and chosenColor1==0:
                        pencolor(colours[int(chosenColor-1)])
                        fillcolor(254/255,254/255,254/255)
                        chosenColor=None
                        chosenColor1=None
                    elif chosenColor>=1 and chosenColor<=9 and chosenColor1>=1 and chosenColor1<=9:
                        color(colours[int(chosenColor-1)], colours[int(chosenColor1-1)])
                        chosenColor=None
                        chosenColor1=None
                    else:
                        tkinter.messagebox.showerror('Error', 'At least one color value is wrong!')
        else:
            Po=False
        
        if is_pressed('e'):
            if Pe==False:
                Pe=True
                tempMovSpd=numinput('Speed Entry', 'Enter custom speed (default:0.0): ', 0.0, 0.00000000001)
                if tempMovSpd!=None:
                    mov_speed=tempMovSpd
        else:
            Pe=False
        if is_pressed('pgdown'):
            if PPD==False:
                PPD=True
                fast=False
                slow=False
                mov_speed=0.1
        else:
            PPD=False
        if is_pressed('pgup'):
            if PPU==False:
                PPU=True
                slow=False
                fast=True
                mov_speed=0.0
        else:
            PPU=False

        if is_pressed('l'):
            if Pl==False:
                Pl=True
                shapeAngl=0
                sideLength=0
                shapeAngl=numinput('Angles','Enter how many angles do you want (it is float proof): ')
                sideLength=numinput('Side Length', 'Enter side length (px, it is float proof too): ')
                if shapeAngl!=None and sideLength!=None:
                    shapeAngl=int(shapeAngl)
                    sideLength=int(sideLength)
                    if shapeAngl>2:
                        if sideLength>0:
                            for i in range(shapeAngl):
                                right(360/shapeAngl)
                                forward(sideLength)
                        else:
                            tkinter.messagebox.showerror('Seriously',"I saw it.\n\nYou tried inputing side length that's equal or smaller than 0!\n\nI'm not a fool. I knew that you can try it and made it ''wrong number'' proof!")
                    else:
                        tkinter.messagebox.showerror('Seriously', "I saw it.\n\nYou tried inputing angles less angles than 3!\nHope you don't input negative side length or one smaller than 0 ;)\n\nI'm not a fool. I knew that you can try it and made it ''wrong number'' proof!")
        else:
            Pl=False
        # additional function keys [ctrl + 'sth']
        if is_pressed('ctrl+s'):
            save.init()
            if type(bgcol)==str:
                converterPStoPNG.convert(bgcol=bgcol)
            else:
                converterPStoPNG.convert(r=bgcol[0],g=bgcol[1],b=bgcol[2])

# tkinter.messagebox.showinfo("Colors", "0.White\n1.Black\n3.Red\nitp.")
# tkinter.messagebox.showinfo("W", "not an err")