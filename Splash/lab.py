import util

class databaseEditor():
    
    def combine_Database(db_loc,first_check,second_check):
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
                        new_Total = int(s_Item['amount'])+int(o_Item['amount'])
                        new_Item['amount'] = new_Total
                        storage_List.append(new_Item)
                        print(storage_List)
                
        #print(original_List,'\n\n', storage_List)
        
databaseEditor.combine_Database('base.json','material','size')
    