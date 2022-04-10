import pytest

from src.santorinai.game.board import Board
from src.santorinai.game.exceptions import InvalidGridReference


def test_board_update():
    board = Board()
    assert board.grid[2, 1] == 0
    # grid 2, 1 (x index 1, y index 2) is B3
    board.update("b3", 2)
    assert board.grid[2, 1] == 2
    # grid 3, 4 (x index 4, y index 3) is E4
    board.update("E4", 3)
    assert board.grid[3, 4] == 3
    board.print()


def test_board_get():
    board = Board()
    board.grid[0, 0] = 4  # 0, 0 maps to a1
    board.grid[1, 2] = 5  # 1, 2 maps to c2
    assert board.get("a1") == 4
    assert board.get("C2") == 5
    assert board.get("e3") == 0


@pytest.mark.parametrize(
    "bad_value",
    [
        "a0",
        "a",
        "",
        1,
        "asd12"
        "t5"
    ]
)
def test_board_invalid_reference(bad_value):
    board = Board()
    with pytest.raises(InvalidGridReference):
        board.update(bad_value, 1)
        board.get(bad_value)
