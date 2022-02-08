import os,cli,util,item
from os import path
url = util.main.goodPath('base.json')
listObj = []

################################################################# USER INTERFACE
#Handles user input and information output
class user_interface():
    cli.face.splash(url,'res\\splash.txt')

face = user_interface
face

##Pyautogui and Web Browser
#Pyperclip
