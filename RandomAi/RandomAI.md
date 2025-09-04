# Gridworld Reinforcement Learning Project

## Overview
This project demonstrates a basic reinforcement learning environment using a simple gridworld. An agent must navigate through a 3x4 grid to reach a goal while avoiding obstacles.

## Project Structure
```
simple-gridworld/
├── gridworld.py           # Environment implementation
├── myAgent.py            # Agent implementation (currently random)
├── demo_gridworld.ipynb  # Jupyter notebook demonstration
├── test_gridworld.py     # Simple test script
└── README.md            # This file
```

## Environment Details

### Grid Layout
- **Size**: 3 rows × 4 columns
- **Agent Start**: Bottom-left corner (0, 2)
- **Goal**: Top-right corner (3, 0) - Green square
- **Obstacle**: Position (1, 1) - Black square
- **Reward**: +1 for reaching goal, 0 otherwise

### Actions
- 0: Move up
- 1: Move right  
- 2: Move down
- 3: Move left

### Rules
- Agent cannot move outside grid boundaries
- Agent cannot move through obstacles
- Episode ends when agent reaches goal
- Maximum of 100 steps per episode

## Setup Instructions

### 1. Virtual Environment Setup
```bash
cd /Users/brockhensley/Downloads/simple-gridworld
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install matplotlib numpy jupyter
```

### 3. Running the Code

#### Option A: Jupyter Notebook (Recommended)
```bash
jupyter lab
# Click on demo_gridworld.ipynb and run cells with Shift+Enter
```

#### Option B: Python Script
```bash
python test_gridworld.py
```

## Code Explanation

### Environment Class (`gridworld.py`)
- `reset()`: Initialize environment to starting state
- `step(action)`: Execute action and return new state, reward, done flag
- `showGrid()`: Create matplotlib visualization of the grid

### RandomAgent Class (`myAgent.py`)
- `getAction(env)`: Returns random action (0-3)
- Serves as baseline for comparison with learning agents

### Demonstration (`demo_gridworld.ipynb`)
1. Creates environment and agent
2. Runs simulation for up to 100 steps
3. Records trajectory of agent movement
4. Generates animated visualization showing path
5. Saves animation as 'plot_grid.gif'

## Expected Output
- Static plot showing grid layout with agent path
- Animated GIF showing agent movement over time
- Random movement pattern (inefficient path to goal)

## Future Extensions
This basic setup can be extended with:
- Q-Learning agent
- Policy Gradient methods  
- Value Iteration algorithm
- Different grid layouts
- Multiple agents
- More complex reward structures

## Troubleshooting

### Virtual Environment Issues
If commands like `pip` or `jupyter` aren't found:
```bash
# Make sure virtual environment is activated
source .venv/bin/activate
# You should see (.venv) in your terminal prompt
```

### Missing Packages
```bash
pip install matplotlib numpy jupyter
```

### Import Errors
Ensure all `.py` files are in the same directory as the notebook.

### Kernel Issues
In Jupyter: Kernel → Restart Kernel to refresh imports.

## Assignment Context
This project is typically the starting point for reinforcement learning coursework. The random agent establishes baseline performance that learning algorithms should significantly improve upon.

Optimal solution requires only 5 moves: Right → Right → Right → Up → Up
Random agent typically takes 20-50+ moves due to inefficient exploration.
