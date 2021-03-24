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
    team_a = Elo(1600)
    team_b = Elo(1500)

    assert round(team_a.point_spread(team_b)) == 7


def test_new_season():

    team_a = Elo(1600)
    team_a._new_season(0.75, 1500)

    assert team_a.elo == 1575


def test_play_game():

    team_a = Elo(1600)
    team_b = Elo(1500)

    team_a.play_game(team_b, 7)

    #write some assertions here when I feel like doing the math by hand

