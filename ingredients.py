class Ingredient:

    def __init__ (self, name:str):
        self.name = name
        self.ingredient_list = {"potato":(0,16,48,16,16),
                                "tomato":(0,0,48,16,16),
                                "onion":(0,32,48,16,16),
                                "chorizo":(0,48,48,16,16),
                                "egg":(0,0,64,16,16)}
        self.image = self.ingredient_list[self.name.lower()]

    @property
    def name (self):
        return self.__name

    @name.setter
    def name (self, name):
        if isinstance (name,str):
            raise TypeError("Ingredients must be strings")
        elif name not in self.__ingredient_list.keys():
            raise ValueError(f"{name} is not a valid ingredient")
        else:
            self.__name = name