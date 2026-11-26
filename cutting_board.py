from station import Station
from dish import Dish
from ingredients import Ingredient

class CuttingBoard(Station):
    '''This is the subclass which stores the cutting board. It is a subclass of the mother class
    Station.'''

    def __init__(self, x:int, y:int, dictionary: dict):
        '''This is the init method of the cutting board subclass.
        :param x: the x coord of the cutting board
        :param y: the y coord of the cutting board
        :param dictionary: used to access the json constants'''
        super().__init__(x,y, dictionary)
        self.__board_ingredients = []

    def chef_acts(self, dish: Dish|None) -> (Dish | None):
        '''This is the inherited method which will be invoked when we act on the cutting board.
        If the ingredient cannot be chopped or is already chopped, it won't do anything.
        :param dish: the dish with which the chef acts, or nothing if the chef is emptyhanded
        :return: if the chef acts with a full dish, it returns an empty dish, having left the ingredients to be chopped
        if the chef acts with an empty dish afterwards it picks up the chopped ingredients
        if the chef acts empty-handed nothing happens'''
        if not isinstance(dish, Dish|None):
            raise TypeError("The chopped object must be in a dish")
        elif isinstance(dish, Dish) and dish.ingredients.raw and len(self.__board_ingredients) == 0 and len(dish.ingredients) > 0:
            for ingredient in dish.ingredients:
                self.__board_ingredients.append(ingredient)

            for element in self.__board_ingredients:
                if element.can_be_chopped() and not element.chopped:
                    element.chopped = True
                    element.raw = False

            dish.empty()

        elif isinstance(dish, Dish) and len(dish.ingredients)==0:
            for element in self.__board_ingredients:
                dish.fill(element)
            self.__board_ingredients = []
        return dish