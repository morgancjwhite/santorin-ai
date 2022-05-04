from contextlib import suppress

GRID_X_AXIS = ["A", "B", "C", "D", "E"]
GRID_Y_AXIS = ["1", "2", "3", "4", "5"]


class Player:
    # Assume a 2 player game!
    def __init__(self, worker_1_position, worker_2_position):
        self.worker_1 = worker_1_position
        self.worker_2 = worker_2_position

    def get_valid_positions(self, worker):
        current_pos = getattr(self, worker)
        print(current_pos)
        x_index = GRID_X_AXIS.index(current_pos[0])
        y_index = GRID_Y_AXIS.index(current_pos[1])
        with suppress(IndexError):
            possible_x_values = [GRID_X_AXIS[i] for i in range(x_index - 1, x_index + 2) if i >= 0]
            possible_y_values = [GRID_Y_AXIS[j] for j in range(y_index - 1, y_index + 2) if j >= 0]
        # TODO Now get all unique combinations of possible x and y values
        print(possible_x_values)
        print(possible_y_values)

    def update_pos(self, worker, position):
        getattr(self, worker)
