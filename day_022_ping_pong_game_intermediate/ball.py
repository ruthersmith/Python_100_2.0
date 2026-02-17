from turtle import Turtle


class Ball(Turtle):
    
    """
        Represents the game ball.

        Handles movement, wall collisions, and paddle bounce behavior.
        Inherits from Turtle for graphical representation.
    """
        
    Y_BOUNDARY = 270
    X_BOUNDARY = 380

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.velocity = 15
        self.moving_x_factor = self.velocity
        self.moving_y_factor = self.velocity
        self.should_reset = False

    def move(self):
        self.handle_collision_with_wall()

        self.goto(self.xcor() + self.moving_x_factor, self.ycor() + self.moving_y_factor)

    def handle_collision_with_wall(self):

        # detects if the ball touches the top of the screen
        if self.ycor() > Ball.Y_BOUNDARY:
            self.moving_y_factor = -1 * self.moving_y_factor

        # detect if the ball touches the right of the screen
        if self.xcor() > Ball.X_BOUNDARY:
            self.should_reset = True
            self.moving_x_factor = -1 * self.moving_x_factor


        # detects if the ball hit the bottom of the screen
        if self.ycor() < (-1 * Ball.Y_BOUNDARY):
            self.moving_y_factor = -1 * self.moving_y_factor

        # detects if the ball hit the left of the screen
        if self.xcor() < (-1 * Ball.X_BOUNDARY):
            self.should_reset = True
            self.moving_x_factor = -1 * self.moving_x_factor

    def reset_pos(self):
        self.goto(0, 0)
        self.should_reset = False