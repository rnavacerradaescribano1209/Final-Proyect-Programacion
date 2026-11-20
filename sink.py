from dish import Dish

class Sink:
    '''This is the class which contains the sink'''
    def __init__(self, x:int, y:int):
        '''This is the init method of the Sink class'''
        self.x = x
        self.y = y

    @property
    def x(self) -> int:
        '''This returns the x coordinate of the sink'''
        return self.__x

    @property
    def y(self) -> int:
        '''This returns the y coordinate of the sink'''
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

    def clean(self) -> Dish:
        '''This is the method which will be invoked when the chef uses the sink
        in order to clean a dirty dish'''

