class Ingredient:
    '''This is the class of the ingredients of the game'''
    INGREDIENT_LIST = {"potato":(0,16,48,16,16),
                        "tomato":(0,0,48,16,16),
                        "onion":(0,32,48,16,16),
                        "chorizo":(0,48,48,16,16),
                        "egg":(0,0,64,16,16)}
    def __init__ (self, name:str):
        '''This is the init method of the class Ingredient.
        :param name: the name of the ingredient'''
        # A new ingredient is always whole
        self.chopped = False
        self.name = name

    @property
    def chopped(self) -> bool:
        '''This tells us whether the ingredient is chopped or not'''
        return self.__chopped
    
    @property
    def name (self) -> str:
        '''This returns the type of ingredient'''
        return self.__name

    @property
    def image(self) -> tuple:
        '''This returns the image tuple of the ingredient'''
        return self.INGREDIENT_LIST[self.name]

    @name.setter
    def name (self, name):
        '''This controls the name'''
        if not isinstance (name,str):
            raise TypeError("Ingredient names must be strings.")
        elif name.lower() not in self.INGREDIENT_LIST.keys():
            raise ValueError(f"{name} is not a valid ingredient. It must be one of these: {str(self.INGREDIENT_LIST)}")
        else:
            self.__name = name.lower()

    @chopped.setter
    def chopped(self, value:bool):
        '''This makes sure chopped is a boolean'''
        if not isinstance(value,bool):
            raise TypeError("Chopped must be a bool")
        else:
            self.__chopped = value