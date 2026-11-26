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
        self.__triturated_ing = self.__dict["ingredients"]["triturated_ingredient_list"]
        self.__cooked_ing = self.__dict["ingredients"]["cooked_ingredient_list"]

        if not isinstance (name,str):
             raise TypeError("Ingredient names must be strings.")
        elif name.lower() not in self.__ingredients.keys():
             raise ValueError(f"{name} is not a valid ingredient. It must be one of these: {list(self.__ingredients)}")
        else:
             self.__name = name.lower()
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
        if self.chopped:
            result = tuple(self.__chopped_ing[self.name])
        elif self.triturated:
            result = tuple(self.__triturated_ing[self.name])
        else:
            if not self.raw:
                result = tuple(self.__cooked_ing[self.name])
            else:
                result = tuple(self.__ingredients[self.name])
        return result

    @chopped.setter
    def chopped(self, value:bool):
        '''This makes sure chopped is a boolean'''
        if not isinstance(value,bool):
            raise TypeError("Chopped must be a bool")
        elif value and not self.can_be_chopped():
            raise ValueError(f"{self.name} cannot be chopped. Only these {list(self.__chopped_ing)}")
        elif self.triturated:
            raise ValueError("A triturated ingredient cannot be chopped.")
        else:
            self.__chopped = value

    @triturated.setter
    def triturated(self, value:bool):
        '''This makes sure triturated is a boolean'''
        if not isinstance(value,bool):
            raise TypeError("Triturated must be a bool")
        elif self.chopped:
            raise ValueError("A chopped ingredient cannot be triturated.")
        # In this case we do not need the method can be triturated since all raw ingredients can be triturated
        else:
            self.__triturated = value

    @raw.setter
    def raw(self, value:bool):
        '''This makes sure raw is a boolean'''
        if not isinstance(value,bool):
            raise TypeError("raw must be a bool")
        elif value and (self.chopped or self.triturated):
            raise ValueError("A chopped or triturated ingredient is not raw.")
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