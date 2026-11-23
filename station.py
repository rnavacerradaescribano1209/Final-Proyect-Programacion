# We need to divide the worktops based on their functionality.
# First, let's code those who dispense things, such as the ingredient boxes, or those that contain dishes.

class Station:

    '''This is the class that corresponds to the mother class of the stations of the game.'''

    def __init__(self, x:int, y:int, dictionary:dict):
        '''This is the init method of the Station class. 
        :param x: the x coord of the station
        :param y: the y coord of the station
        :param dictionary: used to access the json constants. It must be read only in order to be able to
        use it in the subclasses'''
        if not isinstance(dictionary, dict):
            raise TypeError("Dict must be a dictionary")
        else:
            self.__dict = dictionary
        self.x = x
        self.y = y

    @property
    def x(self) -> int:
        '''This returns the x coordinate of the station'''
        return self.__x

    @property
    def y(self) -> int:
        '''This returns the y coordinate of the station'''
        return self.__y

    @property
    def dictionary(self)-> dict:
        '''This returns the dictionary which contains the json constants'''
        return self.__dict

    @x.setter
    def x(self, value:int):
        '''We use this setter to control the values of x'''
        if not isinstance(value,int):
            raise TypeError("The x coord must be an int.")
        elif value<0 or (value+self.__dict['width'])>self.__dict['board_width']:
            raise ValueError("The x coordinate must be within the board limits.")
        else:
            self.__x = value

    @y.setter
    def y(self, value:int):
        '''We use this setter to control the values of y'''
        if not isinstance(value,int):
            raise TypeError("The y coord must be an int.")
        elif value<self.__dict['service_board_height'] or (value+self.__dict['height'])>self.__dict['board_height']:
            # The height cannot be smaller than the service board height 
            raise ValueError("The y coordinate must be within the board limits.")
        else:
            self.__y = value