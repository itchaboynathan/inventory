import os,sys,json
from os import path 

class main():
    def write(data, loc):
        with open(loc, 'w') as json_file:
            json.dump(data, json_file, indent = 4,
                separators = (',', ':'))
            
    def view(obj):
        for item in obj:
            print(' +[Material] '+ item["material"]
                ,' [Size] ' + item["size"]
                ,' [Amount] ' + item["amount"]
                ,'[ID]' + str(item["id"])) 
    
    def combine(loc,tag):
        '''
        if material and size are the same
        get amount
        
        for item in list:
            if item[material] and item[size] are duplicated
                new_amount = item1[amount] + item2[amount]
                delete(item1 & item2)
                create_object(item[material],item[size],new_amount)
        '''
        mylist = []
        temp_list = []
        item_id = [] #incase i wanna use a loop to delte items
        
        if path.isfile(loc)is False: #checks that json file exist
            raise Exception('File not found!') 
        
        with open(loc) as fp: #sets temp list to be the json list
            mylist = json.load(fp)
            
        for item in mylist: #goes through json checks if objects in json are in temp_list, if not it appends them 
           if item[tag] not in temp_list:
                temp_list.append(item[tag])

        mylist = temp_list

        print("List After removing duplicates ", mylist)
        
        