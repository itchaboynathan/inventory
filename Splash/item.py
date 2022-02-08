import os,json,cli,util,item,puck
from os import path

class Item(object):
    name = ''
    amount = 0
    id = 0
    def __init__(self,name,amount,id):
        self.name = name
        self.amount = amount
        self.id = id

#Blueprint for the inventory item
class Puck(object):
    objType = ''
    material = ''
    size = 0
    amount = 0
    id = 0
    def __init__(self,objType,material,size,amount,id):
        self.objType = objType
        self.material = material
        self.size = size
        self.amount = amount
        self.id = id

class Mill_Tool(object):
    objType = ''
    brand = ''
    coated = True
    size = 0.0
    amount = 0
    id = 0
    def __init__(self,objType,brand,coated,size,amount,id):
        self.objType = objType
        self.brand = brand
        self.coated = coated
        self.size = size
        self.amount = amount
        self.id = id

def input_build():
    print('\n')
    url = util.main.goodPath('base.json')
    c_option = ['Puck', 'Tool', 'Consumable']
    m_option = ['Argen','Origin','Wax','Prime']
    s_option = ['10mm','12mm','14mm'
                ,'16mm','18mm','20mm'
                ,'22mm','25mm','30mm']

    cli.face.prompt('res/option_text.txt',3)
    choice = int(input('[Select] '))

    if choice in range(0,len(c_option)):
#choice to start puck input
        if choice == 0:
            cli.face.prompt('res/option_text.txt',0)

            material = int(input('[Select]'))
            if material in range(0,len(m_option)):
                result = m_option[material]
                material = result
            else:
                cli.face.clear()
                cli.face.splash(url)

            cli.face.prompt('res/option_text.txt',1)

            size = int(input('[Select]'))
            if size in range(0,len(s_option)):
                result = s_option[size]
                size = result
            else:
                cli.face.clear()
                cli.face.splash(url)

            amount = input('[Amount?]')

            # See if file exists
            if path.isfile(url)is False:
                raise Exception('File not found!')
            # Otherwise open file
            with open(url) as fp:
                listObj = json.load(fp)
                length = len(listObj)
            id = length + 1

            created_object = item.Puck('Puck',material,size,amount,id)
            util.dictTool.json_save(url,created_object)
            return created_object

#choice to start tool input
        elif choice == 1:
            b_option = ['VHF', 'Amann Girrbach']
            coat_option = [True,False]
            size_option =['2.5mm','2.0mm','1.5mm','0.6mm']
            cli.face.prompt('res/option_text.txt',4)
            brand = int(input('[Select]'))

            if brand in range(0,len(b_option)):
                result = b_option[brand]
                brand = result
            else:
                cli.face.clear()
                cli.face.splash(url)

            cli.face.prompt('res/option_text.txt',5)
            coated = int(input('[Select]'))

            if coated in range(0,len(coat_option)):
                if coated == 0:
                    result = 'True'
                    coated = result
                elif coated == 1:
                    result = 'False'
                    coated = result
            else:
                cli.face.clear()
                cli.face.splash(url)

            cli.face.prompt('res/option_text.txt',6)
            size = int(input('[Select]'))

            if size in range(0,len(size_option)):
                result = size_option[size]
                size = result
            else:
                cli.face.clear()
                cli.face.splash(url)

            amount = input('[Amount?]')
            # See if file exists
            if path.isfile(url)is False:
                raise Exception('File not found!')
            # Otherwise open file
            with open(url) as fp:
                listObj = json.load(fp)
                length = len(listObj)
            id = length + 1

            created_object = item.Mill_Tool('Tool',brand,coated,size,amount,id)
            util.dictTool.json_save(url,created_object)
            return created_object

#choice to start consumable input
        elif choice == 2:
            print()
    else:
        cli.face.clear()
        cli.face.splash(url)
        raise Exception('Input Invalid!')

