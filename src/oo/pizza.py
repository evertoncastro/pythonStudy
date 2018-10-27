
class Pizza(object):

    pieces = 8

    def __init__(self):
        self.ingredients = []

    def self_change_piece(self, pieces):
        self.pieces = pieces

    @classmethod
    def cls_change_piece(cls, pieces):
        cls.pieces = pieces

    def self_add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        print str(self.ingredients)

    def self_remove_ingredient(self):
        self.ingredients.pop()   
        print str(self.ingredients)                        