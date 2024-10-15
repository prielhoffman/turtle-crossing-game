import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

# Setup the screen with a size of 600x600 pixels and turn off automatic updates
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

scoreboard = Scoreboard()
car_manager = CarManager()  # Create car_manager first
player = Player(car_manager, scoreboard)  # Pass the car_manager to Player

# Setup key listeners for player movement
turtle.listen()
turtle.onkey(player.move, "Up")

game_is_on = True

# Main game loop
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move()

    # Detect collision between the player and any car
    for car in car_manager.cars:  # Iterate over all cars
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False  # Stop the game loop

# Close the screen when clicked
screen.exitonclick()
