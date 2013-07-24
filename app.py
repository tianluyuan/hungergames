from __future__ import division, print_function
from Game import Game
from bots import *
from Player import StatusQuo

# Bare minimum test game. See README.md for details.

if __name__ == '__main__':
    players = [Pushover(), Freeloader(), Alternator(), MaxRepHunter(), Random(.2), Random(.8), StatusQuo()]
    game = Game(players)
    game.play_game()
