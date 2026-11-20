# Creating the dish class
class Dish:
    '''This is the class which contains the dishes'''
    def __init__(self, x:int, y:int, dirty: bool):
        '''This is the init method of the Dish class.
        :param x: the x coord of the dish
        :param y: the y coord of the dish'''
        self.x = x
        self.y = y
        self.containing = False
        self.dirty = False

    @property
    def x(self) -> int:
        '''This returns the x coordinate of the dispenser'''
        return self.__x

    @property
    def y(self) -> int:
        '''This returns the y coordinate of the dispenser'''
        return self.__y

    @property
    def containing(self) -> bool:
        return self.__containing 

    @property
    def dirty(self)-> bool:
        return self.__dirty

    @x.setter
    def x(self, value:int):
        '''We use this setter to control the values of x'''
        if not isinstance(value,int):
            raise TypeError("The x coord must be an int.")
        elif value<0 or (value+16)>self.BOARD_WIDTH:
            raise ValueError("The x coordinate must be within the board limits.")
        else:
            self.__x = value

    @y.setter
    def y(self, value:int):
        '''We use this setter to control the values of y'''
        if not isinstance(value,int):
            raise TypeError("The y coord must be an int.")
        elif value<32 or (value+16)>self.BOARD_HEIGHT:
            # The height cannot be smaller than 32 pyxels since that's what the service board takes up
            raise ValueError("The y coordinate must be within the board limits.")
        else:
            self.__y = value

    @containing.setter
    def containing(self, value:bool):
        if not isinstance(value, bool):
            raise TypeError("Containing must be a boolean")

    @dirty.setter
    def dirty(self, value:bool):
        if not isinstance(value, bool):
            raise TypeError("Dirty must be a boolean")

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