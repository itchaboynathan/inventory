import util,os
from os import path,walk

class databaseEditor():
    def save_Database(file_loc):
        if path.isfile(file_loc)is False:
            raise Exception('File not found!')
        listObj = util.dictTool.mount(file_loc)

        listObj.append(object.__dict__)
        util.main.write(listObj,file_loc)

        print()
        
    def combine_Database(db_loc,first_check,second_check,tar_item):
        storage_List = []
        combined_list = []
        
        origin_DB = util.main.goodPath(db_loc)
        original_List = util.dictTool.mount(origin_DB)
        
        for o_Item in original_List: 
            if o_Item not in storage_List:
                storage_List.append(o_Item)
                
                for s_Item in storage_List:     
                    if ((s_Item[first_check] == o_Item[first_check]) and 
                        (s_Item[second_check] == o_Item[second_check])):
                        new_Item = s_Item
                        storage_List.remove(s_Item)
                        new_Total = int(s_Item[tar_item])+int(o_Item[tar_item])
                        new_Item[tar_item] = new_Total
                        storage_List.append(new_Item)
                        print(storage_List)
                
        #print(original_List,'\n\n', storage_List)
t = util.dictTool.index_Folder('res')
#databaseEditor.combine_Database('base.json','material','size','amount')
print(t)    
