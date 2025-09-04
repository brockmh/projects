import random
class RandomAgent:
    def getAction(self, env):
        selected = random.choice(range(env.ACTIONS))
        return selected