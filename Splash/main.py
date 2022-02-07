import os,cli,util,item
from os import path
url = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'base.json')
listObj = []

################################################################# USER INTERFACE
#Handles user input and information output
class user_interface():
    cli.face.splash(url)

face = user_interface
face

##Pyautogui and Web Browser
#Pyperclip
