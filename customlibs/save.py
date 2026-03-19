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

def name():
    a= textinput('File name entry', 'Enter file name: ')
    open("variablesGlobal/filename.txt","w").write(a)
    return a

def init():
    fileName=f"psFiles/{name()}.ps"
    hideturtle()
    Screen().update()
    Screen().getcanvas().postscript(file=fileName,colormode="color")
    showturtle()
    Screen().update()
    open("variablesGlobal/lastSavedFile.txt", "w").write(fileName)
    