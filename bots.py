from Player import BasePlayer
import random

class Pushover(BasePlayer):
    '''Player that always hunts.'''
    def __init__(self):
        self.name = "Pushover"
    
    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        return ['h']*len(player_reputations)

        
class Freeloader(BasePlayer):
    '''Player that always slacks.'''
    
    def __init__(self):
        self.name = "Freeloader"
    
    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        return ['s']*len(player_reputations)
        

class Alternator(BasePlayer):
    '''Player that alternates between hunting and slacking.'''
    def __init__(self):
        self.name = "Alternator"
        self.last_played = 's'
        
    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        hunt_decisions = []
        for i in range(len(player_reputations)):
            self.last_played = 'h' if self.last_played == 's' else 's'
            hunt_decisions.append(self.last_played)

        return hunt_decisions

class MaxRepHunter(BasePlayer):
    '''Player that hunts only with people with max reputation.'''
    def __init__(self):
        self.name = "MaxRepHunter"

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        threshold = max(player_reputations)
        return ['h' if rep == threshold else 's' for rep in player_reputations]


class Random(BasePlayer):
    '''
    Player that hunts with probability p_hunt and
    slacks with probability 1-p_hunt
    '''
    
    def __init__(self, p_hunt):
        self.name = "Random" + str(p_hunt)
        self.p_hunt = p_hunt

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        return ['h' if random.random() < self.p_hunt and len(player_reputations) > 2 else 's' for p in player_reputations]

class FairHunter(BasePlayer):
    '''Player that tries to be fair by hunting with same probability as each opponent'''
    def __init__(self):
        self.name = "FairHunter"

    def hunt_choices(
                self,
                round_number,
                current_food,
                current_reputation,
                m,
                player_reputations,
                ):
        return ['h' if random.random() < rep and len(player_reputations) > 2 else 's' for rep in player_reputations]
        

class SmarterMaxRepHunter(BasePlayer):
    '''Player that hunts only with people with max reputation.'''
    def __init__(self):
        self.name = "SmarterMaxRepHunter"

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        threshold = max(player_reputations)
        return ['h' if rep == threshold and len(player_reputations) > 2 else 's' for rep in player_reputations]
