# Importing the pyxel library
import pyxel
# Importing the Chef class to be able to use it in the Board class
from chef import Chef
from ingredients import Ingredient


class Board:
    """This class contains a simple board"""
    def __init__(self, width: int, height: int):
        """ Method that creates the board.
        :param width: The width of the board
        :param height: The height of the board
        """
        # Setting the attributes
        self.width = width
        self.height = height
        # Adding an attribute to the board which represents the squares of the board. 
        


        # The board will contain a Chef in the middle of it, so one of
        # the attributes of the board will be a Chef object. Note that what is
        # at the middle of the board is the top left corner of the chef.
        self.chef_lower = Chef(self.width // 2, self.height // 3 * 2 ,"lower")
        self.chef_upper = Chef(self.width // 2, self.height // 3 ,"upper")
        # In this init we also need to initialize pyxel
        # This instruction is used to initialize pyxel, see API for more
        # parameters
        pyxel.init(self.width, self.height, title="Pyxel game demo",
                   display_scale=4)
        # Loading the pyxres file with the images
        pyxel.load("sprites.pyxres")
        # Running the game, this will call the update and draw methods in every
        # frame, see API for more
        pyxel.run(self.update, self.draw)

    # Properties and setters
    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @width.setter
    def width(self, width: int):
        if not isinstance(width, int):
            raise TypeError("The width must be an integer")
        elif width < 1:
            raise ValueError("The width must be a positive integer")
        else:
            self.__width = width

    @height.setter
    def height(self, height: int):
        if not isinstance(height, int):
            raise TypeError("The height must be an integer")
        elif height < 1:
            raise ValueError("The height must be a positive integer")
        else:
            self.__height = height

    def update(self):
        """ This is the pyxel method that gets executed in every iteration of
        the game (every frame). You need to put here all the code that has to
        be executed in every frame. Now it contains the logic to exit the
        program if Q key is pressed and to move the chef horizontally if an 
        arrow key is pressed."""
        # To exit the game
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        # To move the chef
        if pyxel.btn(pyxel.KEY_LEFT):
            self.chef_lower.move("left", self.width, self.height)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.chef_lower.move("right", self.width, self.height)
        if pyxel.btn(pyxel.KEY_UP):
            self.chef_lower.move("up", self.width, self.height)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.chef_lower.move("down", self.width, self.height)

        if pyxel.btn(pyxel.KEY_A):
            self.chef_upper.move("left", self.width, self.height)
        if pyxel.btn(pyxel.KEY_D):
            self.chef_upper.move("right", self.width, self.height)
        if pyxel.btn(pyxel.KEY_W):
            self.chef_upper.move("up", self.width, self.height)
        if pyxel.btn(pyxel.KEY_S):
            self.chef_upper.move("down", self.width, self.height)

    def draw(self):
        """This is the pyxel method that gets executed in every iteration of
        the game (every frame). You need to put here all the code to draw the
        sprites of the game.
        """
        # Erasing the previous screen
        pyxel.cls(0)
        # Drawing the chef. Parameters of pyxel.blt are (x, y, sprite_tuple)
        # The * is used to unpack the sprite tuple
        pyxel.blt(0,0,*(1,0,0,192,192))
        pyxel.blt(self.chef_lower.x, self.chef_lower.y, *self.chef_lower.image,colkey=0)
        pyxel.blt(self.chef_upper.x, self.chef_upper.y, *self.chef_upper.image,colkey=0)
        # A text to show the position of the chef, parameters of
        # pyxel.text are (x, y, text, color)
        # pyxel.text(10, 10, f"({self.chef_lower.x}, {self.chef_lower.y})", 7)
        # pyxel.text(10, 20, f"({self.chef_upper.x}, {self.chef_upper.y})", 3)

        if pyxel.btn(pyxel.KEY_RSHIFT):
            pyxel.text(self.chef_lower.x,self.chef_lower.y-8, "ACTION", 7)
        if pyxel.btn(pyxel.KEY_LSHIFT):
            pyxel.text(self.chef_upper.x,self.chef_upper.y-8, "ACTION", 3)

        
