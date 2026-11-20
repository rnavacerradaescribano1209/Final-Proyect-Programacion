from dispenser import Dispenser
from dish import Dish

class DishDispenser(Dispenser):
    '''This is the subclass which stores the dish dispenser. It is a subclass of the mother class
    Dispenser.'''

    def __init__(self, x:int, y:int):
        '''This is the init method of the dish dispenser subclass.'''
        super().__init__(x,y)
        # This is a control variable to know how many dishes were dispensed
        self.__dispensed = 0

    def extract(self) -> (Dish | None):
        '''This is the method which will be invoked when we act on the dish dispenser'''
        if self.__dispensed < self.MAX_DISHES:
            self.__dispensed += 1
            return Dish()  
        return None 