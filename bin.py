from station import Station
from dish import Dish
# Creating a bin class 
class Bin(Station):
    '''This is the Station subclass that contains the bin.'''
    def __init__(self, x:int, y:int,dictionary:dict):
        '''This is the init method of the Bin subclass. 
        :param x: the x coord of the bin
        :param y: the y coord of the bin
        :param dictionary: used to access the json constants'''
        super().__init__(x,y,dictionary)

    def chef_acts(self, dish: Dish) -> (Dish | None):
        '''This inherited method is used to empty the dish when the chef acts on the bin
        :param dish: the dish the chef holds
        :return: an empty dish'''
        if not isinstance(dish, Dish|None):
            raise TypeError("The bin can only empty a dish.")
        else:
            dish.empty()
        return dish