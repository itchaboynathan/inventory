import os,json,item,util
from os import path

class face():
    #method for displaying and banner from file
    def banner(file):
        p = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(p, 'r') as f:
            print(f.read())
            
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def splash(url):
            face.banner('res\\splash.txt')
            person = input('[Terminal]')

            if person  == '1': #View
                face.view(url)
            elif person == '2': #Add
                item.input_build()
                face.clear()
                face.splash(url)
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
                face.clear()
                face.splash(url)

    #Function to display1 what is in Array
    def view(url):
        face.clear()
        face.banner('res/inven.txt')

        if path.isfile(url) is False:
            raise Exception('File not found!')
        with open(url) as fp:
            listObj = json.load(fp)
            sort_data = listObj

        listObj = sorted(sort_data,key = lambda k:k['material'])
        util.main.view(listObj)
        t = input()
        face.clear()
        face.splash(url)

    #method for displaying any prompt from text file
    def prompt(file_path,x):
        p = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)
        l_file = open(p, "r", encoding='utf-8')
        lines = l_file.read()
        option_list = lines.splitlines()

        if x in range(0,len(option_list)):
            choice = option_list[x]
            print(choice.replace('\\n', '\n'))
        else:
            raise Exception('Param not found!')
        l_file.close()
