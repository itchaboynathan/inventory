import os,json,cli,util,item
from os import path


print('\n')
url = 'base.json'

def start():
        m_option = ['Argen','Origin','Wax','Prime']
        s_option = ['10mm','12mm','14mm'
                    ,'16mm','18mm','20mm'
                    ,'22mm','25mm','30mm']

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
        util.dictTool.json_save(url,created_object)
        return created_object
