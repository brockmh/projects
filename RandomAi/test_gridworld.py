"""
Simple test script to run the gridworld environment
Save this as test_gridworld.py and run: python test_gridworld.py
"""

import numpy as np
import matplotlib.pyplot as plt
from gridworld import Environment
from myAgent import RandomAgent

# Create environment and agent
env = Environment()
agent = RandomAgent()

# Reset environment
state = env.reset()

print("Starting Gridworld Simulation")
print("Grid size:", env.GH, "x", env.GW)
print("Agent starts at position:", (env.AGENTS_X, env.AGENTS_Y))
print("Goal is at position:", env.TARGETS_YX[0])
print("Obstacle is at position:", env.OBSTACLES_YX[0])
print("-" * 40)

# Run simulation
trajectory = []
trajectory.append((env.AGENTS_X, env.AGENTS_Y))

max_steps = 100
total_reward = 0

for step in range(max_steps):
    # Agent chooses action
    action = agent.getAction(env)
    
    # Environment processes action
    state, reward, terminal, agent_x, agent_y = env.step(action)
    
    # Track trajectory and rewards
    trajectory.append((agent_x, agent_y))
    total_reward += reward
    
    # Print step info
    action_names = ["UP", "RIGHT", "DOWN", "LEFT"]
    print(f"Step {step+1}: Action={action_names[action]}, Position=({agent_x}, {agent_y}), Reward={reward}")
    
    # Check if goal reached
    if terminal:
        print(f"🎉 Goal reached in {step+1} steps!")
        break
else:
    print(f"😞 Goal not reached after {max_steps} steps")

print(f"Total reward: {total_reward}")
print(f"Final position: {trajectory[-1]}")

# Optional: Display the final grid (requires matplotlib)
try:
    fig, ax = env.showGrid()
    plt.title("Gridworld Environment")
    plt.show()
except:
    print("Note: Install matplotlib to see the grid visualization")
