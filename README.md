# Asteroids 

Based on the classic Asteroids game, this project was built using Python and Pygame as part of the [Boot.dev](https://www.boot.dev) curriculum to enhance OOP skills. This project uses the `uv` project/package manager.

## Features

- **Fluid Movement:** Smooth rotation and player movement.
- **Weapon System:** Rapid-fire projectiles to clear the field of asteroids.
- **Collision Detection:** Precise circular hitboxes for all objects.
- **Split Functionality:** Asteroids split into smaller, faster pieces when hit by a player's shot. 

## Prerequisites 
- Python 3.x (Python 3.13 recommended)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed

## Installation 
```bash
# Clone the repo 
git clone https://github.com/Monolocker/Asteroids.git 

# Navigate to the project folder 
cd Asteroids

# Install dependencies and setup virtual environment 
uv sync 

# Run the game using `uv`
uv run main.py

