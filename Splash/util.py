import os,sys,json
from os import path

class main:
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
        mylist = []
        temp_list = []
        item_id = [] #incase i wanna use a loop to delte items

        if path.isfile(loc)is False: #checks that json file exist
            raise Exception('File not found!')
        with open(loc) as fp: #sets mylist to be the json list
            mylist = json.load(fp)

        for item in mylist: #goes through json checks if objects in json are in temp_list, if not it appends them
            if item not in temp_list:
                temp_list.append(item)
            if item in temp_list:
                new_amount=item[tag] + mylist[tag]
                temp_list.append(item[new_amount])
                mylist[item][tag] = temp_list.append(item[new_amount])
        mylist = temp_list

        print("List After removing duplicates ", mylist)

    def test(loc,tag,tag2,tag3):
        mylist = []
        temp = []

        with open(loc) as fp: #sets mylist to be the json list
            mylist = json.load(fp)
        for item in mylist:
            if item.get(tag) and item.get(tag2) not in temp:
                temp.append(item)
            else:
                if item.get(tag) and item.get(tag2) in temp:
                    newAmount = temp.get(tag3)+item.get(tag3)
                    temp.set(tag3,newAmount)
                    del item
                    mylist = temp
                    setattr(item,'amount',newAmount) ###  <<<<<<<That will change the attribute
                                                        ####     Of the object item and the key 'amount'
                                                        ####     to the newamount
                print('already exist')
        print(temp)
        t= input()
            #print(item.get('amount'))

class dictTool():
    def mount(loc):
        db = []
        with open(loc) as j:
            db = json.load(j)
        return db

    def scan(loc):
        cI = dictTool
        db = cI.mount(loc)
        return db

    def append(obj,target):
        cI = dictTool
        db = cI.mount(target)
        db.append(obj)
        return db

    def json_save(url,object):
        if path.isfile(url)is False:
            raise Exception('File not found!')
        listObj = dictTool.mount(url)

        listObj.append(object.__dict__)
        main.write(listObj,url)
