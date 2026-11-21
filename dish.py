# Creating the dish class
class Dish:
    '''This is the class which contains the dishes'''
    def __init__(self, x:int, y:int, dictionary:dict):
        '''This is the init method of the Dish class.
        :param x: the x coord of the dish
        :param y: the y coord of the dish
        :param dictionary: used to access the json constants'''
        self.__dict = dictionary
        self.x = x
        self.y = y
        self.containing = False
        self.dirty = False

    @property
    def x(self) -> int:
        '''This returns the x coordinate of the dish'''
        return self.__x

    @property
    def y(self) -> int:
        '''This returns the y coordinate of the dish'''
        return self.__y

    @property
    def image(self)-> tuple:
        '''This returns the corresponding dish's images depending on whether it is
        dirty or not'''
        if self.dirty:
            result = (0,48,112,16,16)
        else:
            result = (0,32,80,16,16)
        return result

    @property
    def containing(self) -> bool:
        '''This returns whether the dish already contains something or not'''
        return self.__containing 

    @property
    def dirty(self)-> bool:
        '''This returns whether the dish is dirty or not'''
        return self.__dirty

    @x.setter
    def x(self, value:int):
        '''We use this setter to control the values of x'''
        if not isinstance(value,int):
            raise TypeError("The x coord must be an int.")
        elif value<0 or (value+16)>self.__dict["board_width"]:
            raise ValueError("The x coordinate must be within the board limits.")
        else:
            self.__x = value

    @y.setter
    def y(self, value:int):
        '''We use this setter to control the values of y'''
        if not isinstance(value,int):
            raise TypeError("The y coord must be an int.")
        elif value<self.__dict['service_board_height'] or (value+self.__dict['height'])>self.__dict["board_height"]:
            # The height cannot be smaller than 32 pyxels since that's what the service board takes up
            raise ValueError("The y coordinate must be within the board limits.")
        else:
            self.__y = value

    @containing.setter
    def containing(self, value:bool):
        '''This setter is used to control the values of 'containing'.'''
        if not isinstance(value, bool):
            raise TypeError("Containing must be a boolean")
        else:
            self.__containing = value

    @dirty.setter
    def dirty(self, value:bool):
        '''This setter is used to control the values of 'dirty'.'''
        if not isinstance(value, bool):
            raise TypeError("Dirty must be a boolean")
        else:
            self.__dirty = value

    def fill(self):
        '''This method fills the plate with the corresponding ingredient if
        the dish is not already full of something. If we try to do anything else, 
        this method won't do anything'''
        if not self.containing:
            self.containing = True

    def empty(self):
        '''This method turns a full dish into an empty one, but only if the dish
        was already containing something. Else, this method won't do anything'''
        if self.containing:
            self.containing = False