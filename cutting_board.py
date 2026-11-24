from station import Station
from ingredients import Ingredient

class CuttingBoard(Station):
    '''This is the subclass which stores the cutting board. It is a subclass of the mother class
    Station.'''

    def __init__(self, x:int, y:int,dictionary: dict):
        '''This is the init method of the cutting board subclass.
        :param x: the x coord of the cutting board
        :param y: the y coord of the cutting board
        :param dictionary: used to access the json constants'''
        super().__init__(x,y, dictionary)

    def chef_acts(self, ingredient:Ingredient) -> Ingredient:
        '''This is the inherited method which will be invoked when we act on the cutting board.
        If the ingredient cannot be chopped or is already chopped, it won't do anything.
        :return: a chopped ingredient'''
        if not isinstance(ingredient, Ingredient):
            raise TypeError("The chopped object must be an ingredient")
        elif ingredient.can_be_chopped() == False:
            raise ValueError("This ingredient cannot be chopped")
        elif ingredient.chopped:
            raise ValueError("This ingredient is already chopped")
        else:
            ingredient.chopped = True
        return ingredient