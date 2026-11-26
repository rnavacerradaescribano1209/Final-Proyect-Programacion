import pyxel

class Ingredient:
    '''This is the class of the ingredients of the game'''
    def __init__ (self, name:str, dictionary:dict):
        '''This is the init method of the class Ingredient.
        :param name: the name of the ingredient
        :param dictionary: used to access the constants of the json'''
        self.__dict = dictionary
        self.__ingredients = self.__dict["ingredients"]["ingredients_list"]
        self.__chopped_ing = self.__dict["ingredients"]["chopped_ingredient_list"]

        self.name = name
        # A new ingredient is always whole
        self.chopped = False
        self.triturated = False
        # A new ingredient is always raw
        self.raw = True

    @property
    def chopped(self) -> bool:
        '''This tells us whether the ingredient is chopped or not'''
        return self.__chopped

    @property
    def triturated(self) -> bool:
        '''This tells us whether the ingredient is triturated or not'''
        return self.__triturated

    @property
    def raw(self) -> bool:
        '''This tells us whether the ingredient is raw or not'''
        return self.__raw
    
    @property
    def name(self) -> str:
        '''This returns the type of ingredient'''
        return self.__name

    @property
    def image(self) -> tuple:
        '''This returns the image tuple of the ingredient'''
        if not self.chopped:
            result = tuple(self.__ingredients[self.name])
        else:
            result = tuple(self.__chopped_ing[self.name])
        return result

    @name.setter
    def name(self, name:str):
        '''This controls the name'''
        if not isinstance (name,str):
            raise TypeError("Ingredient names must be strings.")
        elif name.lower() not in self.__ingredients.keys():
            raise ValueError(f"{name} is not a valid ingredient. It must be one of these: {list(self.__ingredients)}")
        else:
            self.__name = name.lower()

    @chopped.setter
    def chopped(self, value:bool):
        '''This makes sure chopped is a boolean'''
        if not isinstance(value,bool):
            raise TypeError("Chopped must be a bool")
        elif value and not self.can_be_chopped():
            raise ValueError(f"{self.name} cannot be chopped. Only these {list(self.__chopped_ing)}")
        else:
            self.__chopped = value

    @triturated.setter
    def triturated(self, value:bool):
        '''This makes sure triturated is a boolean'''
        if not isinstance(value,bool):
            raise TypeError("Triturated must be a bool")
        # In this case we do not need the elif: can be triturated since all ingredients can be triturated
        else:
            self.__triturated = value

    @raw.setter
    def raw(self, value:bool):
        '''This makes sure raw is a boolean'''
        if not isinstance(value,bool):
            raise TypeError("raw must be a bool")
        # Same, we don't need the elif since all of them are raw.
        else:
            self.__raw = value

    # We need the ingredients to be drawn
    def draw(self, x:int, y:int):
        '''This method draws the corresponding ingredient
        :param x: the x where the ingredient is drawn
        :param y: the y where the ingredients is drawn'''

        bank, u, v, width, height = self.image
        pyxel.blt(x,y,bank,u,v,width,height,self.__dict["transparent_color"]) 

    # Adding an auxiliary method to check whether an ingredient can be chopped (eggs can't)
    def can_be_chopped(self)-> bool:
        '''This auxiliary method will return true or false depending on whether the ingredient can be chopped'''
        return self.name in self.__chopped_ing