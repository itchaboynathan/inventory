import os,json
from os import path

class face():
    #method for displaying and banner from file
    def banner(file):
        with open(file, 'r') as f:
            print(f.read())

    #method for displaying any prompt from text file
    def prompt(file_path,x):
        l_file = open(file_path, "r", encoding='utf-8')
        lines = l_file.read()
        option_list = lines.splitlines()

        if x in range(0,len(option_list)):
            choice = option_list[x]
            print(choice.replace('\\n', '\n'))
        else:
            raise Exception('Param not found!')
        l_file.close()
