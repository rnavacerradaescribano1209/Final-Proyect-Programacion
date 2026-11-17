from dispenser import Dispenser
from dish import Dish

class DishDispenser(Dispenser):
    '''This is the subclass which stores the dish dispenser. It is a subclass of the mother class
    Dispenser. It works the same'''

    # We will have 5 dishes available.
    DISHES = [1,2,3,4,5]

    def __init__(self, x:int, y:int):
        '''This is the init method of the dish dispenser subclass.'''
        super().__init__(x,y)
    # This is a control variable to know how many dishes were dispensed
        self.__i = -1

    def dish_extract(self) -> Dish:
        '''This is the method which will be invoked when we act on the dish dispenser'''
        if self.__i < (len(self.DISHES)-1):
            self.__i += 1
            return Dish[self.DISHES(self.__i)]     