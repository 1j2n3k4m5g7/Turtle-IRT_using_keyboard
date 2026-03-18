# Turtle that moves in real time (using your keyboard)
# © 2026 Jan Migo
# Licensed under CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
# Additional permission: Monetized streaming content allowed (YouTube, Twitch, TikTok, Instagram, etc.)
# Paid apps/games/software require separate permission
# Third-party code: Ghostscript (AGPL-3.0) if used

from tkinter.messagebox import showerror, askyesno
from pyperclip import copy
import webbrowser

def init(user_input):
    linkCopyPerm=False
    helpPage=False
    """
    for new codes use template in this function:
    
    `
    elif user_input=="{code}":
        # here goes your script for this code
    `
    ^
    |
    put it between elif and else

    pls leave if, else and first elif THEY ARE CRUTIAL!
    """
    if user_input=="test":
        print("Code Execution Test Passed")
    elif user_input==None:
        pass
    elif user_input=="Help!":
        helpPage=askyesno("Help","Basics:\nW = forward\nS = backward\nA = 15° left\nD = 15° right\n← = thinner line\n→ = thicker line\n↑ = pen up\n↓ = pen down\nPgDn = slower\nPgUp = faster\nlong-press f7 = ignore/don't ignore keys\n \nx = close \n \n \nTO GET MORE INFO VISIT HELP PAGE OR OPEN README FILE (press yes to visit or no/enter to close window)\n\nAfter browser opens please remember about f7\nOpens in default browser (so on Windows it's normally Edge)\nYou can find help page link by typing help.lnk in codes input box\n\nRemember to long-press f7 before and after typing text or so",icon='info',default='no')
        if helpPage:
            webbrowser.open(url="google.com", new=1)
    elif user_input=="help.lnk":
        linkCopyPerm=askyesno('Help Page', 'Page address(link): google.com\n\nCopy to clipboard?')
        if linkCopyPerm:
            copy("google.com")
    else:
        showerror("Code recognition", "Inputed code was not recognized")