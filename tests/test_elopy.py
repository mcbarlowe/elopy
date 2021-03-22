from elopy import __version__
from elopy.elo import Elo


def test_version():
    assert __version__ == "0.1.0"


def test_win_prob():
    team_a = Elo(1600)
    team_b = Elo(1500)

    assert round(team_a.win_probs(team_b), 2) == 0.76


def test_mov_multiplier():

    mult = Elo._mov_multiplier(7, 200)
    assert round(mult, 2) == 0.73


def test_point_spread():
    pass


def test_new_season():
    pass


def test_play_game():
    pass
