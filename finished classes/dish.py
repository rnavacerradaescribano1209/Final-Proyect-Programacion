# Creating the dish class
class Dish:
    '''This is the class which contains the dishes'''
    def __init__(self, x:int, y:int):
        '''This is the init method of the Dish class.
        :param x: the x coord of the dish
        :param y: the y coord of the dish'''
        self.x = x
        self.y = y
        self.containing = False

    @property
    def containing(self) -> bool:
        return self.__containing 

    


