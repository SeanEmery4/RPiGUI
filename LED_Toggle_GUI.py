from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

## Hardware
greenLED = LED(14)
yellowLED = LED(27)
redLED = LED(17)


## GUI
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## Functions
def greenLEDtoggle():
    if greenLED.is_lit:
        greenLED.off()
    else:
        greenLED.on()
        yellowLED.off()
        redLED.off()
        
def yellowLEDtoggle():
    if yellowLED.is_lit:
        yellowLED.off()
    else:
        yellowLED.on()
        greenLED.off()
        redLED.off()
        
def redLEDtoggle():
    if redLED.is_lit:
        redLED.off()
    else:
        redLED.on()
        greenLED.off()
        yellowLED.off()

def close():
    RPi.GPIO.cleanup()
    win.destroy()

## Widgets
greenLEDbutton = Button(win, text = "Turn Green LED on", font = myFont, command = greenLEDtoggle, bg = 'green', height = 2, width = 20)
greenLEDbutton.grid(row = 1, column = 1)

yellowLEDbutton = Button(win, text = 'Turn Yellow LED on', font = myFont, command = yellowLEDtoggle, bg = 'yellow', height = 2, width = 20)
yellowLEDbutton.grid(row = 3, column = 1)

redLEDbutton = Button(win, text = 'Turn Red LED on', font = myFont, command = redLEDtoggle, bg = 'red', height = 2, width = 20)
redLEDbutton.grid(row = 5, column = 1)

exitLEDbutton = Button(win, text = "Exit", font = myFont, command = close, bg = 'white', height = 2, width = 20)
exitLEDbutton.grid(row = 7, column = 1)

win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()
