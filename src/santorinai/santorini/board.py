import numpy as np

BOARD_HEIGHT = 5
BOARD_WIDTH = 5


class Board:
    def __init__(self):
        self.grid = np.zeros((BOARD_HEIGHT, BOARD_WIDTH))
        # self.grid[0, 2] = 1
        print("Starting grid:")
        self.print()

    def print(self):
        output = ["  ".join(map(str, map(int, y))) for y in self.grid]
        print("\n".join(output))
