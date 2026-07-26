Markdown

# Pygame Pac-Man Prototype

A retro-style grid-based Pac-Man prototype built using Python and the **Pygame** library. This project features a custom-built maze layout mapped out with a walls list, a home screen menu state, and player handling logic.

---

## Libraries Used

* **Pygame** (`pygame`) – For rendering graphics, managing game loops, capturing inputs, and handling screen frames.

---

## Installation

Ensure you have Python installed, then install Pygame via pip:

```
cmd
pip install pygame
```

## How to Run

Save your code as pacman.py and run it from your command line:
```
DOS

python pacman.py
```

## Game Controls & Features

    Home Screen: Click the green button (box1) on the start screen to transition into the main game loop (state = 1).

    Movement (WASD):

        W – Move Up

        A – Move Left

        S – Move Down

        D – Move Right

## Development Todo List / Pending Objectives

The following features and mechanics are outlined in the script's development roadmap:

    * Velocity-Based Movement: Refactor movement from teleport-by-position steps to a velocity/speed system (e.g., clicking D sets a constant directional movement vector).

    * Wall Collision Detection: Implement collision detection routines so Pac-Man cannot phase through maze walls (wallslist).

    * Screen Wrapping: Enable horizontal screen wrapping (if Pac-Man goes off the left side of the screen, he respawns on the right side, and vice versa).

    * Pellet System: Implement consumable pellets stored and rendered as a list for Pac-Man to eat and score points.
