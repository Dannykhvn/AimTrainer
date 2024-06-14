# ClickBot

## Introduction

ClickBot is a Python-based game developed using Pygame and Object-Oriented Programming principles. The game features 16-bit pixel art to provide a nostalgic retro aesthetic. It is designed to help improve your aiming skills through a fun and interactive experience.

## Features

- **Retro 16-bit Pixel Art:** Enjoy the nostalgic look and feel of the game with classic pixelated graphics.
- **Dynamic Shapes:** Randomly appearing shapes that you must click to score points.
- **Customizable Game Elements:** Easily adjustable game elements such as shape types, colors, sizes, and speeds.
- **Interactive User Interface:** Intuitive UI elements including buttons and text boxes for a seamless user experience.
- **Score Tracking:** Keep track of your score and see how much you can improve your aiming skills.

## Game Overview

In AimTrainer, your objective is to click on the shapes that appear randomly on the screen within a time limit. Each shape has different characteristics such as color, size, and points value. The game will track your score and display it in real-time. After the time limit is reached, the game will end and display your final score.

## Installation

To run AimTrainer on your local machine, follow these steps:

**Clone the Repository**

   ```bash
   git clone https://github.com/Dannykhvn/ClickBot.git
   cd clickbot
   ```
   
**Set Up a Virtual Environment**

Create and activate a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

**Install Dependencies**

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

**How to Play**

Run the game by executing the following command:

```bash
python main.py
```

Use your mouse to click on the shapes that appear on the screen. Each shape clicked will increase your score based on the shape's point value.

The game will run for a set time limit. Try to achieve the highest score possible within that time.

After the game ends, your final score will be displayed. You can choose to play again or quit the game.

## Code Structure

button.py: Contains the Button class for creating interactive buttons in the game.
constant.py: Stores constants such as shape types and their properties.
shape.py: Defines the Shape class for creating and managing shapes in the game.
textbox.py: Contains the TextBox class for creating and managing text boxes in the game.
base_screen.py: Provides a base class for different screens in the game.
gameover.py: Defines the GameOverScreen class to handle the game over screen logic.
game.py: Contains the GameScreen class which is the main game logic and screen.

## Future Improvements
Additional Shapes: Add more shape types with unique behaviors and point values.
Difficulty Levels: Implement different difficulty levels to challenge players of all skill levels.
Power-Ups: Introduce power-ups that provide temporary bonuses or abilities.


