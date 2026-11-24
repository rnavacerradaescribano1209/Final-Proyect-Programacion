from station import Station
from dish import Dish

class DishDispenser(Station):
    '''This is the subclass which stores the dish dispenser. It is a subclass of the mother class
    Station.'''

    def __init__(self, x:int, y:int,dictionary: dict):
        '''This is the init method of the dish dispenser subclass.
        :param x: the x coord of the dish dispenser
        :param y: the y coord of the dish dispenser
        :param dictionary: used to access the json constants'''
        super().__init__(x,y, dictionary)
        # This is a control variable to know how many dishes were dispensed
        self.__dispensed = 0

    def chef_acts(self, dish: (Dish|None)) -> (Dish | None):
        '''This is the inherited method which will be invoked when we act on the dish dispenser.
        :return: either a Dish object or nothing. If we have already extracted 5 dishes, it will return nothing.
        Otherwise, if the chef is empty handed, it will return a dish. If the chef has a dish it won't do anything'''
        if self.__dispensed < self.dictionary["max_dishes"] and dish is None:
            self.__dispensed += 1
            return Dish(self.x, self.y, self.dictionary)
        return dish