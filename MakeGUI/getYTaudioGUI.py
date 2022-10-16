
import PySimpleGUI as sg
from pytube import YouTube
import os

# folder in user's home
musicFolder="/OneDrive/Music/" 

sg.theme('DarkRed1')   # Add a touch of color

# All the stuff inside your window.
layout = [  [sg.Text('Get youtube audio from a URL')],
            [sg.Text('Copy/Paste URL :'), sg.InputText()],
            [sg.Button('Download'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == "Download":
        yt = YouTube(values[0])
        stream= yt.streams.get_by_itag(140)
        musicFolder="/OneDrive/Music/"
        stream.download(filename = os.path.expanduser("~") + musicFolder +stream.title+".m4a")
window.close()

