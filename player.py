from turtle import Turtle

# Constants for the player's starting position, movement distance, and finish line
STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self, car_manager,scoreboard):  # Accept car_manager as an argument
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.car_manager = car_manager  # Store the reference
        self.scoreboard = scoreboard  # Store the reference

    def move(self):
        # Move the player upwards by the specified movement distance
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        self.check_finish()  # Check if the player has reached the finish line

    def check_finish(self):
        # If the player reaches or exceeds the finish line, reset the position
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)  # Move the player back to the start
            self.car_manager.accelerate()  # Increase the speed of the cars
            self.scoreboard.increment()  # Increase the player's level on the scoreboard