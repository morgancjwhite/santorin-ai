from game.board import Board
from game.exceptions import InvalidGridReference
from game.player import Player

def play_turn():
    pass


if __name__ == '__main__':
    board = Board()
    board.print()
    # board.update("a3", 2)
    # try:
    #     board.update("a6", 4)
    # except InvalidGridReference:
    #     print("error")
    
    # board.print()
    player = Player("B3", "D5")
    player.get_valid_positions("worker_1")