from __future__ import division, print_function
from Game import Game
from bots import *
from Player import Player

# Bare minimum test game. See README.md for details.

players = [SmarterMaxRepHunter(), 
           StatusQuo(), AvgHunter(), AvgSlacker(),
           Alternator(), Freeloader(),
           StatusQuo(), Random(0.3),
           Freeloader(), StatusQuo(), FairHunter(), 
           SmarterMaxRepHunter(), SmarterMaxRepHunter(), 
           StatusQuo(), Random(0.7), ReversePsychologyHunter(),
           FairHunter(), Random(0.5),
           SmarterMaxRepHunter(), SmarterMaxRepHunter(), 
           StatusQuo(), FoodTatForTit(), 
           FairHunter(),
           FoodTitForTat(), StatusQuoSlacker()]

game = Game(players)

if __name__ == '__main__':
    game.play_game()
