from ingredients import Ingredient

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
        self.ingredients = []
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
            result = self.__dict["dirty_dish_image"]
        else:
            result = self.__dict["clean_dish_image"]
        return result

    @property
    def ingredients(self) -> list:
        '''This returns what the dish contains'''
        return self.__ingredients 

    @property
    def dirty(self)-> bool:
        '''This returns whether the dish is dirty or not'''
        return self.__dirty

    @x.setter
    def x(self, value:int):
        '''We use this setter to control the values of x'''
        if not isinstance(value,int):
            raise TypeError("The x coord must be an int.")
        elif value<0 or (value+self.__dict['width'])>self.__dict["board_width"]:
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

    @ingredients.setter
    def ingredients(self, value:list):
        '''This setter is used to control the values of 'ingredients'.'''
        if not isinstance(value, list):
            raise TypeError("Ingredients must be a list")
        for element in value:
            if not isinstance(element, Ingredient):
                raise TypeError("The elements of ingredients must be Ingredient.")
        self.__ingredients = value

    @dirty.setter
    def dirty(self, value:bool):
        '''This setter is used to control the values of 'dirty'.'''
        if not isinstance(value, bool):
            raise TypeError("Dirty must be a boolean")
        else:
            self.__dirty = value

    def fill(self, ingredient: Ingredient):
        '''This method fills the plate with the corresponding ingredient
        :param ingredient: the ingredient which is added to the dish'''
        if not isinstance(ingredient, Ingredient):
            raise TypeError("What we add to the dish must be an Ingredient")
        else:
            self.ingredients.append(ingredient)

    def empty(self):
        '''This method turns a full dish into an empty one (empties the containing list)'''
        self.ingredients = []