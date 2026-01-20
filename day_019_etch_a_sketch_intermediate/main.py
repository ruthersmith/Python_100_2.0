"""
    Author: Ruthersmith Bercy

    Interactive Etch A Sketch program.

    This module simulates the classic Etch A Sketch drawing toy, a mechanical
    drawing device invented by André Cassagnes of France.
    More information: https://en.wikipedia.org/wiki/Etch_A_Sketch

    The program is fully interactive and allows the user to:
    - Move the drawing pen around the screen using the arrow keys
    - Clear the screen by pressing the 'c' key
    - Toggle drawing behavior using:
        - 'u' for pen up (movement without drawing)
        - 'd' for pen down (movement draws on the screen)

    The pen starts in the pen-down position by default.
    
    How to run:
    python main.py
     
"""

from turtle import Turtle, Screen


class EtchASketch:

    """
        Controls an interactive Etch A Sketch drawing application.

        This class manages user input, drawing behavior, and screen
        interactions to simulate an Etch A Sketch toy. Keyboard events
        are bound to movement and control methods, allowing the user to
        draw, move, and clear the screen.

        The application is started by calling the `run()` method.
    """

    MOVE_FORWARD_KEY = "Up"
    MOVE_BACKWARD_KEY = "Down"
    ROTATE_CLOCKWISE_KEY = "Right"
    ROTATE_COUNTER_CLOCKWISE_KEY = "Left"

    CLEAR_SCREEN_KEY = "c"

    PEN_UP_KEY = "u"
    PEN_DOWN_KEY = "d"

    MOVEMENT_SPEED = 10
    ROTATION_SPEED = 10

    def __init__(self):
        self.tim = Turtle()
        # Screen object controls the window when we run our code
        self.screen = Screen()

    def move_forwards(self):
        """Moves the pen forward by a fixed distance determined by EtchASketch.MOVEMENT_SPEED"""
        self.tim.forward(EtchASketch.MOVEMENT_SPEED)

    def move_backwards(self):
        """Moves the pen backward by a fixed distance determined by EtchASketch.MOVEMENT_SPEED"""
        self.tim.backward(EtchASketch.MOVEMENT_SPEED)

    def rotate_clockwise(self):
        """Rotates the pen clockwise by a fix angle determined by EtchASketch.ROTATION_SPEED"""
        self.tim.right(EtchASketch.ROTATION_SPEED)

    def rotate_counter_clockwise(self):
        """Rotates the pen counter-clockwise by a fix angle determined by EtchASketch.ROTATION_SPEED"""
        self.tim.left(EtchASketch.ROTATION_SPEED)

    def pen_up(self):
        """Pull the pen up -- no drawing when moving."""
        self.tim.penup()

    def pen_down(self):
        """Pull the pen down -- drawing when moving."""
        self.tim.pendown()

    def clear_screen(self):
        """Clear the screen and resets"""
        self.tim.clear()
        self.tim.reset()

    def run(self):
        """
            Starts the Etch A Sketch application.
            Binds keyboard controls, initializes the drawing state
        """
        # exist to allow us to start listening for events
        self.screen.listen()
        # movement/drawing listeners
        self.screen.onkeypress(fun=self.move_forwards, key=EtchASketch.MOVE_FORWARD_KEY)
        self.screen.onkeypress(fun=self.move_backwards, key=EtchASketch.MOVE_BACKWARD_KEY)
        self.screen.onkeypress(fun=self.rotate_clockwise, key=EtchASketch.ROTATE_CLOCKWISE_KEY)
        self.screen.onkeypress(fun=self.rotate_counter_clockwise, key=EtchASketch.ROTATE_COUNTER_CLOCKWISE_KEY)
        # clear the screen listener
        self.screen.onkey(fun=self.clear_screen, key=EtchASketch.CLEAR_SCREEN_KEY)
        # pen control listeners
        self.screen.onkey(fun=self.pen_up,key=EtchASketch.PEN_UP_KEY)
        self.screen.onkey(fun=self.pen_down,key=EtchASketch.PEN_DOWN_KEY)
        # Shut the turtle graphics window when mouse clicks on the Screen
        self.screen.exitonclick()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sketch_pad = EtchASketch()
    sketch_pad.run()