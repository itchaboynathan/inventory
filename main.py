import os,json,cli,util,item
from os import path
url = 'base.json'
listObj = []
#Biggest test yet
################################################################## VIEW FUNCTION
#Function to display1 what is in Array
def view():
    user_interface.clear()
    cli.face.banner('res/inven.txt')

    if path.isfile(url) is False:
        raise Exception('File not found!')
    with open(url) as fp:
        listObj = json.load(fp)
        sort_data = listObj

    listObj = sorted(sort_data,key = lambda k:k['material'])
    util.main.view(listObj)
    t = input()
    user_interface.clear()
    user_interface.splash()

################################################################# USER INTERFACE
#Handles user input and information output
class user_interface():
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def splash():
        cli.face.banner('res/splash.txt')
        person = input('[Terminal]')

        if person  == '1': #View
            view()
        elif person == '2': #Add
            item.input_build()
            user_interface.clear()
            user_interface.splash()
        elif person == '3': #Remove
            print()
        elif person == '4': #New Item
            print()
        elif person == '5': #Help
            #util.main.test(url)
            print()
        elif person == '6':
            print(util.dictTool.cleanScan(url))
            t = input()
        else:
            user_interface.clear()
            user_interface.splash()

face = user_interface
face.splash()

##Pyautogui and Web Browser
#Pyperclip
