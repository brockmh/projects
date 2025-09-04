import numpy as np
import copy
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

class Environment(object):
    def __init__(self):
        # Initialize elements of the task environment
        self.GH = 3  # Height of gridworld
        self.GW = 4  # Width of gridworld
        self.AGENT = 240.0  # Pixel values of agents
        self.TARGETS = [150.0]  # Pixel values of targets
        self.AGENTS_X = 0  # x-coordinates of initial locations of agents
        self.AGENTS_Y = self.GH - 1  # y-coordinates of initial locations of agents
        self.OBSTACLE = 100.0
        self.OBSTACLES_YX = [(self.GH - 2, 1)]
        self.TARGETS_YX = [(0, self.GW - 1)]  # Locations of the target
        self.REWARDS = [1]
        self.ACTIONS = 4  # Move up, down, left, right

    def reset(self):
        '''
        Reset the environment.
        '''
        self.s_t = np.zeros([self.GH, self.GW], dtype=np.float64)
        self.agents_x = copy.deepcopy(self.AGENTS_X)
        self.agents_y = copy.deepcopy(self.AGENTS_Y)
        self.agent_status = False
        self.s_t[self.agents_y][self.agents_x] += self.AGENT
        for l, p in zip(self.TARGETS_YX, self.TARGETS):
            self.s_t[l[0]][l[1]] = p
        for yx in self.OBSTACLES_YX:
            self.s_t[yx[0]][yx[1]] = self.OBSTACLE
        return self.s_t

    def step(self, action):
        '''
        Change environment state based on actions.
        :param action: List of integers providing actions for each agent
        '''
        dx, dy = self.getDelta(action)
        targetx = self.agents_x + dx
        targety = self.agents_y + dy
        reward = 0
        terminal = False
        if self.noCollision(targetx, targety):
            for a, r in zip(self.TARGETS, self.REWARDS):
                if self.s_t[targety][targetx] == a:
                    reward = r
                    terminal = True
                    break
            self.s_t[self.agents_y][self.agents_x] -= self.AGENT
            self.s_t[targety][targetx] += self.AGENT
            self.agents_x = targetx
            self.agents_y = targety
        return self.s_t, reward, terminal, self.agents_x, self.agents_y

    def getDelta(self, action):
        '''
        Determine the direction that the agent should take based on the action selected.
        :param action: int
        '''
        if action == 0:
            return 0, -1
        elif action == 1:
            return 1, 0
        elif action == 2:
            return 0, 1
        elif action == 3:
            return -1, 0
        elif action == 4:
            return 0, 0

    def noCollision(self, x, y):
        '''
        Check if the x, y coordinate is currently empty.
        :param x: Int, x coordinate
        :param y: Int, y coordinate
        '''
        if (
            x < 0
            or x >= self.GW
            or y < 0
            or y >= self.GH
            or self.s_t[y][x] == self.OBSTACLE
        ):
            return False
        else:
            return True

    def showGrid(self):
        self.palette = ListedColormap(["w", "k", "g"])
        walls = np.zeros([self.GH, self.GW])
        walls[self.OBSTACLES_YX[0][0], self.OBSTACLES_YX[0][1]] = 1

        num_target = len(self.TARGETS_YX)
        targets = np.zeros([num_target, self.GH, self.GW])
        for i in range(num_target):
            targets[i, self.TARGETS_YX[i][0], self.TARGETS_YX[i][1]] = 1

        image_mat = copy.deepcopy(walls)
        for i in range(num_target):
            image_mat += (i + 2) * targets[i, :, :]
        
        self.figure, self.ax = plt.subplots()
        self.ax.plot(self.AGENTS_X, self.AGENTS_Y, 'ok', markersize=10)
        self.ax.matshow(image_mat, cmap=self.palette)
        
        return self.figure, self.ax
