from station import Station
from ingredients import Ingredient

class IngredientDispenser(Station):
    '''This is the subclass which stores the ingredient dispensers. It is a subclass of the mother class
    Dispenser.'''

    def __init__(self, x:int, y:int,dictionary: dict, content:str):
        '''This is the init method of the ingredient dispensers subclass.
        :param x: the x coord of the ingredient dispensers
        :param y: the y coord of the ingredient dispensers
        :param dictionary: used to access the json constants
        :param content: the content (ingredient) which is dispensed'''
        super().__init__(x,y, dictionary)
        self.content = content

    @property
    def content(self)-> str:
        '''This is the property which returns the content parameter'''
        return self.__content

    @content.setter
    def content(self, value:str):
        '''This is the content setter, which will help us control the values that the content can take'''
        if not isinstance(value, str):
            raise TypeError("The content must be a str")
        elif value.lower() not in self.dictionary['conts']:
            raise ValueError(f"The content must be one of these: {list(self.dictionary['conts'])}")
        else:
            self.__content = value

    def chef_acts(self) -> Ingredient:
        '''This is the method which was inherited which will be invoked when we act on the ingredient dispensers.
        :return: the corresponding ingrdient'''
        return Ingredient(self.content, self.dictionary)