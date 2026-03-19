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

from PIL import Image
from os import remove
from tkinter import messagebox as msg
from pathlib import Path

# main

def convert(bgcol=None,r=None,g=None,b=None):
    orginalFile=open("variablesGlobal/lastSavedFile.txt", "r").read()
    fileName=open("variablesGlobal/filename.txt", "r").read()
    pngPath=f"imagesPNG/{fileName}.png"
    
    Image.open(orginalFile).load(scale=4)
    Image.open(orginalFile).save(pngPath, "png")
    remove("variablesGlobal/lastSavedFile.txt")
    remove("variablesGlobal/filename.txt")
    if Path(pngPath).is_file():
        bialy=False
        if g==254 and r==254 and b==254:
            bialy=True
        
        # Open the image
        img = Image.open(pngPath).convert("RGBA")

        # Get data
        data = img.getdata()
        
        # Create a new data list
        new_data = []
        for item in data:
            # If the pixel is white (255,255,255)
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                if bgcol=='black':
                    new_data.append((0, 0, 0, item[3]))
                elif bgcol=='red':
                    new_data.append((255, 0, 0, item[3]))
                elif bgcol=='orange':
                    new_data.append((255, 165, 0, item[3]))
                elif bgcol=='yellow':
                    new_data.append((255, 255, 0, item[3]))
                elif bgcol=='green':
                    new_data.append((0, 128, 0, item[3]))
                elif bgcol=='blue':
                    new_data.append((0, 0, 255, item[3]))
                elif bgcol=='violet':
                    new_data.append((238, 130, 238, item[3]))
                elif bgcol=='pink':
                    new_data.append((255, 192, 203, item[3]))
                elif bgcol=='gray':
                    new_data.append((128, 128, 128, item[3]))
                elif bgcol=='white' or bialy==True:
                    new_data.append((254, 254, 254, item[3]))
            else:
                new_data.append(item)
        
        # Update image data
        img.putdata(new_data)
        
        # Save the result
        img.save(pngPath)
        msg.showinfo("File info", "FILE SAVED SUCCESSFULLY")
    else:
        msg.showerror("FILE ERROR", "FILE WAS NOT CREATED")