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
    material = ''
    size = 0
    amount = 0
    id = 0
    def __init__(self,material,size,amount,id):
        self.material = material
        self.size = size
        self.amount = amount
        self.id = id
        
class Mill_Tool(object):
    brand = ''
    coated = True
    size = 0.0
    amount = 0
    id = 0
    def __init__(self,material,size,amount,id):
        self.material = material
        self.size = size
        self.amount = amount
        self.id = id
