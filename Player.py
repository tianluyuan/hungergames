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


class StatusQuo(BasePlayer):
    '''
    Your strategy starts here.
    '''
    def __init__(self):
        self.name = "StatusQuo"
        self.total_expeditions = 0

    def initial_choices(self, player_reputations):
        return ['h']*len(player_reputations)
            
    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        '''Required function defined in the rules'''
        # Keep track of over number of hunts+slacks
        self.total_expeditions += len(player_reputations)

        if round_number == 1:
            return self.initial_choices(player_reputations)

        # Calculate the median reputation
        arr_reputations = np.array(player_reputations)
        median_reputation = np.median(arr_reputations)
        
        # Calculate the number of hunts needed to match median rep
        hunts_so_far = self.total_expeditions * current_reputation
        hunts_for_median = (self.total_expeditions+len(player_reputations))*median_reputation
        
        hunts_needed = hunts_for_median - hunts_so_far
        
        n_highest_reputations = heapq.nlargest(hunts_needed, player_reputations)

        choices = ['s']*len(player_reputations)
        for rep in n_highest_reputations:
            player_to_hunt_with = player_reputations.index(rep)
            
            choices[player_to_hunt_with] = 'h'

        return choices
        
    def hunt_outcomes(self, food_earnings):
        '''Required function defined in the rules'''
        pass
        

    def round_end(self, award, m, number_hunters):
        '''Required function defined in the rules'''
        pass
        
