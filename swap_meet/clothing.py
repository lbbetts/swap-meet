from .item import Item

class Clothing:

    def __init__(self, category="Clothing", condition=0):
        self.category = category
        self.condition = condition
        self.condition_description = Item.condition_description(self, condition)
    
    def __str__(self):
        return "The finest clothing you could wear."