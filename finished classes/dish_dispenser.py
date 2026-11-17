from dispenser import Dispenser
from dish import Dish

class DishDispenser(Dispenser):
    '''This is the subclass which stores the dish dispenser. It is a subclass of the mother class
    Dispenser. It works the same'''

    # We will have 5 dishes available.
    DISHES = [1,2,3,4,5]
    # This is a control variable to know how many dishes were dispensed
    i = -1

    def __init__(self, x:int, y:int):
        '''This is the init method of the dish dispenser subclass.'''
        super().__init__(x,y)

    def dish_extract(self) -> Dish:
        '''This is the method which will be invoked when we act on the dish dispenser'''
        if self.i < 4:
            self.i += 1
            return Dish[self.i]     