
from ingredients import Ingredient
# We need to divide the worktops based on their functionality.
# First, let's code those who dispense things, such as the ingredient boxes, or those that contain dishes.

class Dispenser:

    '''This is the class that corresponds to the ingredient boxes and dish pile.'''
    BOARD_WIDTH = 192
    BOARD_HEIGHT = 176
    CONTS = ['dish','chorizo','egg','onion','tomato','potato']

    def __init__(self, x:int, y:int, content:str):
        '''This is the init method of the Dispenser class. 
        :param x: the x coord of the dispenser
        :param y: the y coord of the dispenser
        :param content: the content dispensed by the dispenser (dish, ingredient)'''
        self.x = x
        self.y = y
        self.content = content

    @property
    def x(self) -> int:
        '''This returns the x coordinate of the dispenser'''
        return self.__x

    @property
    def y(self) -> int:
        '''This returns the y coordinate of the dispenser'''
        return self.__y

    @property
    def content(self) -> str:
        '''This returns the content of the dispenser'''
        return self.__content

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

    @content.setter
    def content(self, cont:str):
        '''We use this setter to control the values of the content'''
        if not isinstance(cont, str):
            raise TypeError("The content must be a str.")
        elif cont not in self.CONTS:
            raise ValueError("The content must be one of these:" + str(self.CONTS))
        else:
            self.__content = cont
   
    def extract(self) -> Ingredient:
        '''This method dispenses the corresponding ingredient-class object'''
        return Ingredient(self.content)