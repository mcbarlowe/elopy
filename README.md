# Elopy

This is a module to allow you to maintain state for teams as you progress them
through games played against opponents. This uses the the constants set out
from [538's NBA Elo](https://fivethirtyeight.com/features/how-we-calculate-nba-elo-ratings/). But
you could inherit and overload the functions to work for any sport you wanted.

Code Examples:

```
from elopy.elo import Elo

team_a = Elo(start_elo=1600, k=20, hca = 100)
team_b = Elo(start_elo=1400, k=20, hca = 100)

#To get the win probability of team_a beating team_b at home

team_a_probs = team_a.win_probs(team_b, is_home=True)

#To get the win probability of team_b beating team_a at home

team_b_probs = team_b.win_probs(team_a, is_home=True)

#If you want to get away probabilities then set is_home to False

#To get the point spread of team_a vs. team_b. Positive represents an underdog
#negative represents a favorite

#at home
point_spread_home = team_a.point_spread(team_b, is_home=True)

#not at home. Will return a value
point_spread_away = team_a.point_spread(team_b, is_home=False)

#update elo's after a team has played the other. Let's say team a beat team b
#by 15 points as a visitor

team_a.play_game(team_b, 15, is_home=False)

#This will update both team a and team b's Elo ratings. If you run the same line
as above again it will be as if both teams are playing a second game

team_a.play_game(team_b, 15, is_home=False)

#This means that team a played team b again and beat them by 15 points again as
the visitor


