"""Elo Calculator

This is a project to create an Elo class to model a team so you can keep passing
it other Elo team objects and have it store its Elo state/value as they play
games throughout the season/s or however the user wants to do it.

Most of these formulas come from 538s NBA Elo model found here
https://fivethirtyeight.com/features/how-we-calculate-nba-elo-ratings/
"""


class Elo:
    def __init__(self, start_elo: int = 1500, k: int = 20, hca: int = 100) -> None:
        """
        Parameters:
        start_elo - the prior Elo rating of the team/player defaults to average
        k         - k value of Elo system defaults to 20 for NBA from 538 model
        hca       - Home court advantage. Again defaults to 100 the 538 value

        Returns:
        """
        self.elo = start_elo
        self._k = k
        self._hca = hca

    @staticmethod
    def _mov_multiplier(mov, elo_diff: int) -> float:
        """
        Returns Margin of Victory multiplier for team. Would need to overload
        this in an inherited class for a different sport
        """
        return (mov + 3) ** 0.8 / (7.5 + 0.006 * elo_diff)

    def _new_season(self, percent_kept: float, regression_value: int) -> None:
        """
        converting team's elo for new season again this formula comes from 538
        """
        self.elo = (self.elo * percent_kept) + ((1 - percent_kept) * regression_value)

    def win_probs(self, opponent: "Elo", is_home: bool = True) -> float:
        """
        Returns the win probability against opponent of team Elo instance
        calling the function.
        So if :
        teama = Elo()
        teamb = Elo()
        teama.win_probs(teamb, is_home=True)

        that will return the win probability of team a playing at home against
        team b

        Parameters:
        opponent:    - another Elo instance representing the opposing team
        is_home      - boolean representing whether the Elo instance call the
                       win_probs function is home or away
        Returns:     Win probability of team
        """
        if is_home:
            hca = self._hca
        else:
            hca = 0

        return 1 / (10 ** ((-1 * ((self.elo + hca) - opponent.elo)) / 400) + 1)

    def point_spread(self, opponent: "Elo", is_home: bool = True) -> float:
        """
        Returns the point spread for the team calling the function against the
        team passed as opponent. So if the result is positive the team is an
        underdog, if negative the favorite.

        Parameters:
        opponent    - Elo instance representing opponent
        is_home     - boolean representing whether the Elo instance call the
                       win_probs function is home or away
        Returns:     Point spread of team
        """
        if is_home:
            hca = self._hca
        else:
            hca = 0

        return ((self.elo - opponent.elo) + hca) / 28

    def play_game(
        self, opponent: "Elo", point_difference: int, is_home: bool = True
    ) -> None:
        """
        Updates both teams Elo values given who won or lost the game and elo
        points won or lost are modified by the MOV modifier and Home court
        advantage.

        Parameters:
        opponent     - Elo instance representing opponent
        is_home      - boolean representing whether the Elo instance call the
                       win_probs function is home or away
        Returns:
        """
        win_prob = self.win_probs(opponent, is_home)
        win = 1 if point_difference > 0 else 0
        if is_home:
            hca = self._hca
        else:
            hca = 0

        prior_elo = self.elo
        prior_opponent_elo = opponent.elo
        if point_difference > 0:
            self.elo = prior_elo + (
                (self._k * (win - win_prob))
                * self._mov_multiplier(
                    point_difference, (prior_elo + hca) - prior_opponent_elo
                )
            )
        else:
            self.elo = prior_elo + (
                self._k
                * (win - win_prob)
                * self._mov_multiplier(
                    -1 * point_difference, (prior_opponent_elo - (prior_elo + hca))
                )
            )

        elo_diff = self.elo - prior_elo
        opponent.elo = opponent.elo + (-1 * elo_diff)
