from station import Station
from dish import Dish

class Sink(Station):
    '''This is the Station subclass which contains the sink'''
    def __init__(self, x:int, y:int, dictionary:dict):
        '''This is the init method of the Sink subclass'''
        super().__init__(x,y,dictionary)

    def chef_acts(self, dish: (Dish|None)) -> Dish|None:
        '''This is the inherited method which will be invoked when the chef uses the sink
        in order to clean a dirty dish
        :return: a clean dish'''
        if not isinstance(dish,( Dish|None)):
            raise TypeError("The object to be cleaned must be a dish")
        elif dish.dirty:
            dish.dirty = False
        return dish