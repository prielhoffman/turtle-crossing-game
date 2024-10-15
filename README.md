# Turtle Crossing Game

This is a Python implementation of a **Turtle Crossing Game** using the `turtle` graphics library. The player controls a turtle that attempts to cross the screen while avoiding randomly moving cars. With each successful crossing, the game's difficulty increases by accelerating the speed of the cars.

## Features
* Player moves a turtle upwards using the "Up" key.
* Cars appear randomly and move across the screen horizontally.
* If the turtle collides with a car, the game ends.
* Each time the turtle successfully reaches the top of the screen, the level increases and the cars move faster.

## Modules
The game is divided into the following modules:
- **main.py**: Controls the game flow, including player movement, car generation, and collision detection.
- **player.py**: Defines the `Player` class, which manages the turtle's movements and interactions with the finish line.
- **car_manager.py**: Defines the `CarManager` class, responsible for creating and moving cars across the screen.
- **scoreboard.py**: Defines the `Scoreboard` class, which keeps track of the player's level and displays the "Game Over" message.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/turtle-crossing-game.git
    cd turtle-crossing-game
    ```

2. Install the required dependencies (if needed):
    ```bash
    pip install turtle
    ```

3. Run the game:
    ```bash
    python main.py
    ```

## How to Play
1. Use the **Up** arrow key to move the turtle upwards.
2. Avoid the moving cars as they cross the screen.
3. Each time you reach the top of the screen, the level increases, and the cars speed up.
4. If the turtle collides with a car, the game ends.
