import os,json,cli,util,item
from os import path
url = 'base.json'
listObj = []

####################################################################################BUILD OBJECT FUNCTION
#Creates a new inventory item when called
def build(material,size,amount,id):
    print('\n')
    m_option = ['Argen','Origin','Wax','Prime']
    s_option = ['10mm','12mm','14mm'
                ,'16mm','18mm','20mm'
                ,'22mm','25mm','30mm']
    
    cli.face.prompt('res/option_text.txt',0)
    
    material = int(input('[Select]'))
    if material in range(0,len(m_option)): 
        result = m_option[material]
        material = result
    else:
        user_interface.clear()
        user_interface.splash() 
        
    cli.face.prompt('res/option_text.txt',1)
    
    size = int(input('[Select]'))
    if size in range(0,len(s_option)):
        result = s_option[size]
        size = result
    else:
        user_interface.clear()
        user_interface.splash() 
        
    amount = input('[Amount?]')
    
    # See if file exists
    if path.isfile(url)is False:
        raise Exception('File not found!')  
    # Otherwise open file
    with open(url) as fp:
        listObj = json.load(fp)
        length = len(listObj)
    id = length + 1

    created_object = item.Puck(material,size,amount,id)
    
    json_save(created_object)
    return created_object

#################################################################################### VIEW FUNCTION
def view():
    user_interface.clear()
    cli.face.banner('res/inven.txt')
    
    if path.isfile(url)is False:
        raise Exception('File not found!') 
    with open(url) as fp:
        listObj = json.load(fp)
        sort_data = listObj
        
    listObj = sorted(sort_data,key = lambda k:k['material'])
    util.main.view(listObj)
    t = input()
    user_interface.clear()
    user_interface.splash()

#################################################################################### SAVE FUNCTION
#Function to save and append to objects created
def json_save(object): 
    
    if path.isfile(url)is False:
        raise Exception('File not found!') 
    with open(url) as fp:
        listObj = json.load(fp)
        
        #combine duplicates code goes here
        
        
    listObj.append(object.__dict__)
    util.main.write(listObj,url)
    
#################################################################################### USER INTERFACE 
#Handles user input and information output                                         
class user_interface():
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def splash():
        material = ''
        size = 0
        amount = 0
        id = 0
        cli.face.banner('res/splash.txt')
        
        person = input('[Terminal]')
        if person  == '1': #View
            view()
        elif person == '2': #Add
            build(material,size,amount,id)
            user_interface.clear()
            user_interface.splash()
        elif person == '3': #Remove
            print()
        elif person == '4': #New Item
            print()
        elif person == '5': #Help
            util.main.test(url)
            print()
        elif person == '6':
            util.main.combine(url)
            t = input()
        else:
            user_interface.clear()
            user_interface.splash()
    
face = user_interface
face.splash()

##Pyautogui and Web Browser
#Pyperclip
