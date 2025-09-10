import pytest
from projects.p001_number_guess.app import Game


def test_game_init_bounds():
    with pytest.raises(ValueError):
        Game(10, 5)
    with pytest.raises(ValueError):
        Game(1, 10, 0)


def test_guessing():
    g = Game(1, 1_000, 3)
    g.secret = 50  # deterministisch
    assert g.guess(10) == "higher"
    assert g.guess(90) == "lower"
    assert g.guess(50) == "correct"