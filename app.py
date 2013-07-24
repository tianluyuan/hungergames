from __future__ import division, print_function
from Game import Game
from bots import *
from Player import StatusQuo, FoodTitForTat

# Bare minimum test game. See README.md for details.

players = [Freeloader(), StatusQuo(), FairHunter(), 
           SmarterMaxRepHunter(), SmarterMaxRepHunter(), 
           StatusQuo(), 
           Freeloader(), FairHunter(), 
           SmarterMaxRepHunter(), SmarterMaxRepHunter(), 
           StatusQuo(), Random(0.3),
           Freeloader(), StatusQuo(), FairHunter(), 
           SmarterMaxRepHunter(), SmarterMaxRepHunter(), 
           StatusQuo(), Random(0.7),
           Freeloader(), FairHunter(), 
           SmarterMaxRepHunter(), SmarterMaxRepHunter(), 
           StatusQuo(),  
           Freeloader(), FairHunter(), StatusQuo(),
           FoodTitForTat()]

game = Game(players)

if __name__ == '__main__':
    game.play_game()
