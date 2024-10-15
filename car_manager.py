from turtle import Turtle
import random

# Constants for car properties and movement
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []
        self.create_car()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.car_creation_counter = 0  # Initialize a counter to control car creation

    def create_car(self):
        # Create a new car (a square turtle) with a random color and position
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(1, 2)
        new_car.color(random.choice(COLORS))
        y_axis = random.randint(-250, 250)
        new_car.goto(250, y_axis)
        self.cars.append(new_car)

    def move(self):
        # Move all cars to the left by the current move distance
        for car in self.cars:
            car.goto(car.xcor() - self.move_distance, car.ycor())

        # Increment the counter to track when to create a new car
        self.car_creation_counter += 1

        # Create a new car every 6 iterations of the game loop
        if self.car_creation_counter >= 6:
            self.create_car()
            self.car_creation_counter = 0  # Reset the counter

    def accelerate(self):
        # Increase the speed of all cars
        self.move_distance += MOVE_INCREMENT
