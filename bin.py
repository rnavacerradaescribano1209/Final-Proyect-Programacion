from dish import Dish
# Creating a bin class 
class Bin:
    '''This is the class that contains the bin.'''
    BOARD_WIDTH = 192
    BOARD_HEIGHT = 176
    def __init__(self, x:int, y:int):
        '''This is the init method of the Bin class. 
        :param x: the x coord of the bin
        :param y: the y coord of the bin'''
        
        self.x = x
        self.y = y

    @property
    def x(self) -> int:
        '''This returns the x coordinate of the bin'''
        return self.__x

    @property
    def y(self) -> int:
        '''This returns the y coordinate of the bin'''
        return self.__y

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

    def empty_dish(self, dish: Dish):
        '''This method is used to empty the dish when the chef acts on the bin
        :param dish: the dish the chef holds'''
        if isinstance(dish, Dish):
            dish.empty()
        else:
            raise TypeError("The bin can only empty a dish.")