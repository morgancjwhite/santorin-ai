import numpy as np

from src.santorinai.game.exceptions import InvalidGridReference

BOARD_HEIGHT = 5
BOARD_WIDTH = 5


class Board:
    def __init__(self):
        self.grid = np.zeros((BOARD_HEIGHT, BOARD_WIDTH))
        self.letter_coord = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4 }
        self.num_coord = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4 }

    def print(self):

        each_line = ["  ".join(map(str, map(int, y))) for y in self.grid]
        coordinated = [f"{num} | {line}" for num, line in zip([1, 2, 3, 4, 5], each_line)]
        print("    A  B  C  D  E\n   --------------")
        print("\n".join(coordinated))

    def update(self, coordinate, value):
        self.grid[self._grid_coord_conversion(coordinate)] = value

    def get(self, coordinate):
        return self.grid[self._grid_coord_conversion(coordinate)]

    def _grid_coord_conversion(self, coordinate):
        try:
            if len(coordinate) != 2:
                raise InvalidGridReference
            x = self.letter_coord[coordinate[0].lower()]
            y = self.num_coord[coordinate[1].lower()]

        except (KeyError, TypeError) as exc:
            raise InvalidGridReference from exc
        return y, x
