from turtle import Turtle

# Font settings for the scoreboard
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        # Clear the previous score and write the new level
        self.clear()
        self.goto(-250,250)
        self.write(self.level, align = "center", font = FONT)

    def increment(self):
        # Increase the level by 1 and update the scoreboard
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        # Display "Game Over" in the center of the screen
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER!", align = "center", font = FONT)