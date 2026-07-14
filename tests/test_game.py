from src.game import Game


def test_gutter_game_scores_zero():
    game = Game()
    for _ in range(20):
        game.roll(0)
    assert game.score() == 0


def test_one_spare_scores_bonus():
    game = Game()
    game.roll(5)
    game.roll(5)  # 스페어
    game.roll(3)
    for _ in range(17):
        game.roll(0)
    assert game.score() == 16
