from __future__ import division, print_function
from Game import Game
from bots import *
from Player import Player

# Bare minimum test game. See README.md for details.

players = [SmarterMaxRepHunter(), Player(),
           Alternator(),
           StatusQuo(), Random(0.3),
           Freeloader(), StatusQuo(), FairHunter(),]
           # SmarterMaxRepHunter(), SmarterMaxRepHunter(), 
           # StatusQuo(), Random(0.7), ReversePsychologyHunter(),
           # StatusQuo(), Random(0.3),
           # Freeloader(), StatusQuo(), FairHunter(), 
           # SmarterMaxRepHunter(), SmarterMaxRepHunter(), 
           # StatusQuo(), Random(0.7), ReversePsychologyHunter(),
           # StatusQuo(), Random(0.3),
           # Freeloader(), StatusQuo(), FairHunter(), 
           # SmarterMaxRepHunter(), SmarterMaxRepHunter(), 
           # StatusQuo(), Random(0.7), ReversePsychologyHunter(),
           # StatusQuo(), Random(0.3),
           # Freeloader(), StatusQuo(), FairHunter(), 
           # SmarterMaxRepHunter(), SmarterMaxRepHunter(), 
           # StatusQuo(), Random(0.7), ReversePsychologyHunter(),
           # StatusQuo(), FoodTatForTit(), 
           # FairHunter(), AverageHunter(),
           # BoundedHunter(0.7,1.0),
           # FoodTitForTat(), StatusQuoSlacker()]

game = Game(players)

if __name__ == '__main__':
    game.play_game()
