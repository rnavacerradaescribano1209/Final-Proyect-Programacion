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
        # The board will contain a Chef in the middle of it, so one of
        # the attributes of the board will be a Chef object. Note that what is
        # at the middle of the board is the top left corner of the chef.
        self.chef1 = Chef(self.width // 2, self.height // 3 * 2 ,"lower")
        self.chef2 = Chef(self.width // 2, self.height // 3 ,"upper")
        # In this init we also need to initialize pyxel
        # This instruction is used to initialize pyxel, see API for more
        # parameters
        pyxel.init(self.width, self.height, title="Pyxel game demo",
                   display_scale=4)
        # Loading the pyxres file with the images
        pyxel.load("assets/example.pyxres")
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
            self.chef1.move("left", self.width, self.height)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.chef1.move("right", self.width, self.height)
        if pyxel.btn(pyxel.KEY_UP):
            self.chef1.move("up", self.width, self.height)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.chef1.move("down", self.width, self.height)

        if pyxel.btn(pyxel.KEY_A):
            self.chef2.move("left", self.width, self.height)
        if pyxel.btn(pyxel.KEY_D):
            self.chef2.move("right", self.width, self.height)
        if pyxel.btn(pyxel.KEY_W):
            self.chef2.move("up", self.width, self.height)
        if pyxel.btn(pyxel.KEY_S):
            self.chef2.move("down", self.width, self.height)

    def draw(self):
        """This is the pyxel method that gets executed in every iteration of
        the game (every frame). You need to put here all the code to draw the
        sprites of the game.
        """
        # Erasing the previous screen
        pyxel.cls(0)
        # Drawing the chef. Parameters of pyxel.blt are (x, y, sprite_tuple)
        # The * is used to unpack the sprite tuple
        pyxel.blt(self.chef1.x, self.chef1.y, *self.chef1.image)
        pyxel.blt(self.chef2.x, self.chef2.y, *self.chef2.image)
        # A text to show the position of the chef, parameters of
        # pyxel.text are (x, y, text, color)
        pyxel.text(10, 10, f"({self.chef1.x}, {self.chef1.y})", 7)
        pyxel.text(10, 20, f"({self.chef2.x}, {self.chef2.y})", 3)

        ingredient_list=("Potato","Tomato","Onion","Chorizo","Egg")
        j = 10
        for i in ingredient_list:
            pyxel.text(self.__width-50,j,i,7)
            j+=10

        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.text(self.chef1.x,self.chef1.y-8, "ACTION", 7)
        if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT):
            pyxel.text(self.chef2.x,self.chef2.y-8, "ACTION", 3)

        
