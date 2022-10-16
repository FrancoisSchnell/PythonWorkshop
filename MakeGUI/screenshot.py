from PIL import Image, ImageGrab
import PySimpleGUI as sg

# Init
screenshotNumber = 1

# All the stuff inside your window.
layout = [ [sg.Button('Screenshot!'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('A screenshot tool!', layout, size=(300,50))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == "Screenshot!":
        im = ImageGrab.grab()
        im.save("MakeGUI/screenshots/"+str(screenshotNumber)+".png")
        screenshotNumber += 1   
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

window.close()

