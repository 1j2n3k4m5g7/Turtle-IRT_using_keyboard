# Turtle that moves in real time (using your keyboard)
# © 2026 Jan Migo
# Licensed under CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
# Additional permission: Monetized streaming content allowed (YouTube, Twitch, TikTok, Instagram, etc.)
# Paid apps/games/software require separate permission

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
    