import pyxel
import json

# Creating a class called Square, which will represent a square of the board. 
class Square:
    '''This class contains the squares of the board.'''

    def __init__(self, value: str,dictionary:dict):
        ''' The init method of the class.
        :param value: the squares can either be part of the service board, floor, worktop, hand-over worktops,
        wall, ingredients boxes, blender, server, bin, cutting board, pan, plates, or return platform'''
        
        self.__dict = dictionary

        if not isinstance(value, str):
            raise TypeError("The value of square must be a string.")
        elif value.lower() not in self.__dict["images"]:
            raise ValueError("The value must be " + str(tuple(self.__dict["images"])))
        else:
            self.__value = value.lower()

        self.is_active = False

    @property
    def value(self) -> str:
        '''This method will return the value of value.
        :return: the type of square'''
        return self.__value

    # @property
    # def dictionary(self) -> dict:
    #     return self.__dict

    # @dictionary.setter
    # def dictionary(self,dictionary:dict):
    #     if not isinstance(dictionary,dict):
    #         raise TypeError("Square must recieve a dictionary")
    #     else:
    #         self.__dict = dictionary

    def __str__(self) -> str:
        '''We invoke this method in order to make sure we are working with the right square, although it's not essential here.
        :return: the type of the square'''
        return self.value

    def __repr__(self) -> str:
        '''We invoke the method to show the name we want when it is written in the interpreter.
        :return: again, the type of the square'''
        return self.__str__()

    def __eq__(self, other) -> bool:
        '''We invoke this method to compare two objects of the class Square.
        In addition to self it must receive the other object. 
        It must return True or False.
        :param other: the second square we want to compare the first one with
        :return: whether the squares are equal or not. 
        In case they are not both Square objects, it will return False.'''
        if isinstance(other, Square):
            return (self.value == other.value)
        else:
            return NotImplemented

    def draw(self, x:int, y:int):
        '''This is the pyxel method that draws the square.
        In this case, we are drawing the squares.
        :param x: the x coord where the square is drawn
        :param y: the y coord where the square is drawn'''
        # Unpacking the tuple
        bank, u, v, width, height = self.__dict["images"][self.value]
        pyxel.blt(x, y, bank, u, v, width, height)