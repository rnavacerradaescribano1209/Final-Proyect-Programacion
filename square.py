import pyxel

# Creating a class called Square, which will represent a square of the board. 
class Square:
    '''This class contains the squares of the board. The width and height of the squares are constant.'''
    WIDTH = 16
    HEIGHT = 16
    # Its image must be read-only.
    # Assigning a read-only image for each type of square using a dictionary: (The tuple means (image bank, u, v, width,height))
    IMAGES = {'service_board': (1, 0, 0, 192, 32), 'floor': (0, 0, 32, 16, 16), 'worktop': (0, 16, 32, 16, 16), 
        'hand_over_wt': (0, 48, 32, 16, 16), 'wall': (0, 32, 32, 16, 16), 'tomato_box': (0, 0, 48, 16, 16),
        'chorizo_box': (0, 48, 48, 16, 16), 'egg_box': (0, 0, 64, 16, 16), 'onion_box': (0, 32, 48, 16, 16), 
        'potato_box': (0, 16, 48, 16, 16),'blender': (0, 32, 176, 16, 16), 'server': (0, 32, 160, 16, 16), 
        'bin': (0, 48, 160, 16, 16), 'cutting_board': (0, 16, 176, 16, 16), 'pan': (0, 48, 176, 16, 16),
        'plates': (0, 0, 176, 16, 16), 'return_platform': (0, 48, 112, 16, 16), 'sink': (0,16,64,16,16) }

    def __init__(self, value: str):
        ''' The init method of the class.
        :param value: the squares can either be part of the service board, floor, worktop, hand-over worktops,
        wall, ingredients boxes, blender, server, bin, cutting board, pan, plates, or return platform'''

        if not isinstance(value, str):
            raise TypeError("The value of square must be a string.")
        elif value.lower() not in self.IMAGES:
            raise ValueError("The value must be " + str(tuple(self.IMAGES)))
        else:
            self.__value = value.lower()

    @property
    def value(self) -> str:
        '''This method will return the value of value.
        :return: the type of square'''
        return self.__value

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
        bank, u, v, width, height = self.IMAGES[self.value]
        pyxel.blt(x, y, bank, u, v, width, height)
