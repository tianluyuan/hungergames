# This file is intended to be a final submission. python tester.py Player.py
# should work at all times. If it does not, there is a bug.
# If you're just trying to test a solution, scroll down to the Player
# class.

# This file is intended to be in the same format as a valid solution, so
# that users can edit their solution into Player and then submit just this
# file to the contest. If you see any reason this would not work, please submit
# an Issue to https://github.com/ChadAMiller/hungergames/issues or email me.

# You can see more sample player classes in bots.py
import numpy as np
import heapq

class BasePlayer(object):
    '''
    Base class so I don't have to repeat bookkeeping stuff.
    Do not edit unless you're working on the simulation.
    '''
    def __init__(self):
        self.total_expeditions = 0
        self.total_food_earnings = 0
        self.food_earnings = []

    def __str__(self):
        try:
            return self.name
        except AttributeError:
            # Fall back on Python default
            return super(BasePlayer, self).__repr__()
    
    def hunt_choices(*args, **kwargs):
        raise NotImplementedError("You must define a strategy!")
        
    def hunt_outcomes(*args, **kwargs):
        pass
        
    def round_end(*args, **kwargs):
        pass

    def get_num_hunts_needed(self, current_reputation, ideal_reputation, n_partners_remaining):
        # Keep track of over number of hunts+slacks
        # Calculate the number of hunts needed to match median rep
        hunts_so_far = self.total_expeditions * current_reputation
        hunts_for_ideal = (self.total_expeditions+n_partners_remaining)*ideal_reputation
        
        hunts_needed = int(hunts_for_ideal - hunts_so_far)

        self.total_expeditions += n_partners_remaining
        
        return hunts_needed


class Player(BasePlayer):
    def __init__(self):
        """
        Optional __init__ method is run once when your Player object is created before the
        game starts

        You can add other internal (instance) variables here at your discretion.

        You don't need to define food or reputation as instance variables, since the host
        will never use them. The host will keep track of your food and reputation for you
        as well, and return it through hunt_choices.
        """
        super(Player, self).__init__()

    # All the other functions are the same as with the non object oriented setting (but they
    # should be instance methods so don't forget to add 'self' as an extra first argument).

    def hunt_choices(self, round_number, current_food, current_reputation, m,
            player_reputations):
        hunt_decisions = ['h' for x in player_reputations] # replace logic with your own
        return hunt_decisions

    def hunt_outcomes(self, food_earnings):
        pass # do nothing

    def round_end(self, award, m, number_hunters):
        pass # do nothing
