import pyxel
# Creating a class called Square, which will represent a square of the board. 

class Square:
    '''This class contains the squares of the board.'''
    def __init__(self, value: str):
        ''' The init method of the class.
        :param value: the squares can either be part of the service board, floor, worktop, hand-over worktops,
        wall, ingredients boxes, blender, server, bin, cutting board, pan, plates, or return platform
        :param x: width of the square
        :param y: height of the square'''
        # Its width, height and image must be read-only.

        WIDTH = 16
        HEIGHT = 16

        # Assigning a read-only image for each type of square using a dictionary:
        images = {'service_board': (0, 0, 192, 192, 32), 'floor': (1, 0, 0, 192, 48), 'worktop': (0, 16, 32, 16, 16), 
                'hand_over_wt': (0, 48, 32, 16, 16), 'wall': (0, 32, 32, 16, 16), 'tomato_box': (0, 0, 48, 16, 16),
            'chorizo_box': (0, 48, 48, 16, 16), 'egg_box': (0, 0, 64, 16, 16), 'onion_box': (0, 32, 48, 16, 16), 
            'potato_box': (0, 16, 48, 16, 16),'blender': (0, 32, 176, 16, 16), 'server': (0, 32, 160, 16, 16), 
            'bin': (0, 48, 160, 16, 16), 'cutting_board': (0, 16, 176, 16, 16), 'pan': (0, 48, 176, 16, 16),
            'plates': (0, 0, 176, 16, 16), 'return_platform': (0, 48, 112, 16, 16)}

        if not isinstance(value, str):
            raise TypeError("The value of square must be a string.")
        elif value.lower() not in images.keys:
            raise ValueError("The value must be" + str(TYPE))
        else:
            self.__value = value.lower()



        # if value == 'service_board':
        #     self.image = (0, 0, 192, 192, 32)
        # elif value == 'floor':
        #     self.image = (1, 0, 0, 192, 48)
        # elif value == 'worktop':
        #     self.image = (0, 16, 32, 16, 16)
        # elif value == 'hand_over_wt':
        #     self.image = (0, 48, 32, 16, 16)
        # elif value == 'wall':
        #     self.image = (0, 32, 32, 16, 16)
        # elif value == 'tomato_box':
        #     self.image = (0, 0, 48, 16, 16)     
        # elif value == 'onion_box':
        #     self.image = (0, 32, 48, 16, 16)
        # elif value == 'egg_box':
        #     self.image = (0, 0, 64, 16, 16)
        # elif value == 'chorizo_box':
        #     self.image = (0, 48, 48, 16, 16)
        # elif value == 'potato_box':
        #     self.image = (0, 16, 48, 16, 16)
        # elif value == 'blender':
        #     self.image = (0, 32, 176, 16, 16)
        # elif value == 'server':
        #     self.image = (0, 32, 160, 16, 16)
        # elif value == 'bin':
        #     self.image = (0, 48, 160, 16, 16)
        # elif value == 'cutting_board':
        #     self.image = (0, 16, 176, 16, 16)
        # elif value == 'pan':
        #     self.image = (0, 48, 176, 16, 16)
        # elif value == 'plates':
        #     self.image = (0, 0, 176, 16, 16)
        # elif value == 'return_platform':
        #     self.image = (0, 48, 112, 16, 16)
