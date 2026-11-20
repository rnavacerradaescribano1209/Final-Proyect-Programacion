from dish import Dish

class DirtyDish(Dish):
    '''This is the Dirty Dish subclass.'''
    def __init__(self, x:int, y:int):
        '''This is the init method of the Dirty Dish subclass.
        :param x: the x coord of the dirty dish
        :param y: the y coord of the dirty dish'''
        super().__init__(x,y)

        