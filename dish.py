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

    def fill(self) -> Dish:
        '''This method fills the plate with the corresponding ingredient if
        the dish is not already full of something'''
        if not self.containing:
            self.containing = True
            return Dish(self.containing)

    def empty(self)-> Dish:
        '''This method turns a full dish into an empty one, but only if the dish
        was already containing something'''
        if self.containing:
            self.containing = False
            return Dish(self.containing)