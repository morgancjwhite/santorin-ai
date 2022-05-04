from santorinai.game.player import Player


def test_player_possible_locations():
    player = Player("A2", "A3")
    player = player.get_valid_positions("worker_1")
