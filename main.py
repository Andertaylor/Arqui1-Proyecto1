"""
Tecnológico de Costa Rica
Proyecto Individual 1 - Arqui 1
Anderson Taylor Cordero
"""

import base64
import cv2
import PIL.Image
import PIL.ImageTk
import pygame
import numpy as np
import tkinter
from io import BytesIO
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import *
from pygame import *
from tkinter import *

"""
_____Constants_____
Are defined the constant values used in the code, like strings, integers, and so on.
"""
MAXVALUE = 255
BG = "white"
COUNTER = 0
DPI = 100
FILTERBN = "tucan2.jpg"
FIGURE_SIZE  = (4, 3)
GRAY = 'gray'
HFPLACEX = 650
HFPLACEY = 410
HOPLACEX = 650
HOPLACEY = 50
IM_WIDTH = 299
IM_HEIGHT= 280
IMG_SIZE = (640, 480)
NW = 'nw'
ONE = 1
ORIGINAL = "tucan.jpg"
PLOT = 111
POS_ORIGINAL = (100, 70)
POS_FILTER   = (100, 370)
SCREEN_SIZE  = ('1050x900')
SCALE_SIZE   = (299, 299)
TITLE = "Arqui1-Proyecto1"
TWO = 2
ZERO = 0

"""
____Aux functions to get binary values
"""

#Convert to binary
def toBinary(n):
    n = bin(n)
    nString = str(n)
    nString = nString[TWO:]
    nStringPadded = '0' * (8 - len(nString)) + nString
    return nStringPadded

#Write data in file
def writeFile(data):
    file = open(r"demo.txt", 'a')
    for i in data:
        file.write(i)
    file.close()

#Get binary data from file
def getBinary():
    img = cv2.imread(r"tucan2.jpg", cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, IMG_SIZE)
    plt.imshow(img, cmap=GRAY)
    binary_img = []
    for row in img:
        binary_img += list(map(toBinary, row))
    print(binary_img)
    writeFile(binary_img)

"""
_____Main screen_____
The main logic of the project is coded in order to load the images, create the histograms and prepare the
date so the assembler code con work better.

"""

#Screen design
screen = tkinter.Tk()
screen.geometry(SCREEN_SIZE)
screen.configure(background=BG)
screen.title(TITLE)

#Images imported and scale
tkOriginal = PIL.Image.open(ORIGINAL)
tkFilterbn = PIL.Image.open(FILTERBN)
tkOriginal = PIL.ImageTk.PhotoImage(tkOriginal.resize(SCALE_SIZE, PIL.Image.ANTIALIAS))
tkFilterbn = PIL.ImageTk.PhotoImage(tkFilterbn.resize(SCALE_SIZE, PIL.Image.ANTIALIAS))

#Histigram creation from the matrix given by OpenCV libraries
original  = pygame.image.load(ORIGINAL)
imgFilter = pygame.image.load(FILTERBN)
originalHist = cv2.imread(ORIGINAL, ZERO)
filterHist   = cv2.imread(FILTERBN, TWO)

#Draw the histogram using Tkinter libraries
originFigure = Figure(figsize = FIGURE_SIZE, dpi = DPI)
filterFigure = Figure(figsize = FIGURE_SIZE, dpi = DPI)
originHistGraph = originFigure.add_subplot(PLOT)
filterHistGraph = filterFigure.add_subplot(PLOT)

setOriginFigure = FigureCanvasTkAgg(originFigure, master=screen)
setFilterFigure = FigureCanvasTkAgg(filterFigure, master=screen)
setOriginFigure.draw()
setFilterFigure.draw()

#Place the canvas
canvasOriginal = tkinter.Canvas(screen, width = IM_WIDTH, height = IM_HEIGHT)
canvasFilterbn = tkinter.Canvas(screen, width = IM_WIDTH, height = IM_HEIGHT)
canvasOriginal.create_image(ONE, ONE, anchor =NW, image = tkOriginal)
canvasFilterbn.create_image(ONE, ONE, anchor =NW, image = tkFilterbn)
setOriginFigure.get_tk_widget().place(x=HOPLACEX, y=HOPLACEY)
setFilterFigure.get_tk_widget().place(x=HFPLACEX, y=HFPLACEY)
canvasOriginal.place(x=HOPLACEY, y=HOPLACEY)
canvasFilterbn.place(x=HOPLACEY, y=HFPLACEY)

#Creating the histogram
arrayX = []
arrayYOrigin = []
arrayYFilter = []
ix  = COUNTER
iyo = COUNTER
iyf = COUNTER

for ix in range(ZERO, MAXVALUE):
    arrayX.append(ix + ONE)
    arrayYOrigin.append(ZERO)
    arrayYFilter.append(ZERO)
    ix = ix + ONE
for iyo in originalHist:
    for j in iyo:
        arrayYOrigin[j - ONE] = arrayYOrigin[j - ONE] + ONE
for iyf in filterHist:
    for j in iyf:
        arrayYFilter[j - ONE] = arrayYFilter[j - ONE] + ONE

#Creating the bar histogram
graphicOrigin = originHistGraph.bar(arrayX, arrayYOrigin)
graphicFilter = filterHistGraph.bar(arrayX, arrayYFilter)

getBinary()

#Main loop
screen.mainloop()



