from Player import BasePlayer
import numpy as np
import heapq
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

class FoodTitForTat(BasePlayer):
    '''
    Your strategy starts here.
    '''
    name = "FoodTitForTat"

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
        if round_number == 1:
            return self.initial_choices(player_reputations)
        choices = ['h' if food_earned_last >= 0 else 's' for food_earned_last in self.food_earnings]
        return choices[0:len(player_reputations)]

    def hunt_outcomes(self, food_earnings):
        '''Required function defined in the rules'''
        self.total_food_earnings += sum(food_earnings)
        self.food_earnings = food_earnings

    def round_end(self, award, m, number_hunters):
        '''Required function defined in the rules'''
        pass

class StatusQuo(BasePlayer):
    '''
    Your strategy starts here.
    '''
    name = "StatusQuo"

    def initial_choices(self, player_reputations):
        return ['h'] * len(player_reputations)
            
    def get_num_hunts_needed(self, current_reputation, player_reputations):
        # Calculate the median reputation
        arr_reputations = np.array(player_reputations)
        median_reputation = np.median(arr_reputations)
                
        # Keep track of over number of hunts+slacks
        # Calculate the number of hunts needed to match median rep
        hunts_so_far = self.total_expeditions * current_reputation
        hunts_for_median = (self.total_expeditions+len(player_reputations))*median_reputation
        # print hunts_so_far, hunts_for_median
        
        hunts_needed = int(hunts_for_median - hunts_so_far)

        self.total_expeditions += len(player_reputations)
        
        return hunts_needed

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        '''Required function defined in the rules'''        
        hunts_needed = self.get_num_hunts_needed(current_reputation, player_reputations)

        if round_number == 1:
            return self.initial_choices(player_reputations)

        # Default choices is to always slack
        choices = ['s']*len(player_reputations)

        if hunts_needed < 1 or len(player_reputations) < 3:
            return choices

        n_highest_reputations = heapq.nlargest(hunts_needed, player_reputations)
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

class AvgHunter(BasePlayer):
    '''Player that hunts only probability equal to the mean of all other reputations'''
    def __init__(self):
        self.name = "AvgHunter"

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        mean = 1 if round_number == 1 else np.mean(np.array(player_reputations))
        return ['h' if random.random() < mean and len(player_reputations) > 2 else 's' for rep in player_reputations]

class AvgSlacker(BasePlayer):
    '''Player that slacks with probability equal to the mean of all other reputations'''
    def __init__(self):
        self.name = "AvgSlacker"

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):

        mean = 1 if round_number == 1 else 1-np.mean(np.array(player_reputations))
        return ['h' if random.random() < mean and len(player_reputations) > 2 else 's' for rep in player_reputations]

class StatusQuoSlacker(BasePlayer):
    '''
    Your strategy starts here.
    '''
    def __init__(self):
        super(StatusQuoSlacker, self).__init__()
        self.name = "StatusQuoSlacker"

    def initial_choices(self, player_reputations):
        return ['h'] * len(player_reputations)
            
    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        '''Required function defined in the rules'''        
        # Calculate the median reputation
        arr_reputations = np.array(player_reputations)
        median_reputation = np.median(arr_reputations)
        hunts_needed = self.get_num_hunts_needed(current_reputation, median_reputation,
                                                 len(player_reputations))

        if round_number == 1:
            return self.initial_choices(player_reputations)

        # Default choices is to always hunt
        choices = ['h']*len(player_reputations)

        if hunts_needed < 1 or len(player_reputations) < 3:
            return choices

        n_highest_reputations = heapq.nlargest(hunts_needed, player_reputations)
        for rep in n_highest_reputations:
            player_to_hunt_with = player_reputations.index(rep)
            
            choices[player_to_hunt_with] = 's'

        return choices
        
    def hunt_outcomes(self, food_earnings):
        '''Required function defined in the rules'''
        pass
        

    def round_end(self, award, m, number_hunters):
        '''Required function defined in the rules'''
        pass

class FoodTatForTit(BasePlayer):
    '''
    Your strategy starts here.
    '''
    name = "FoodTatForTit"

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
        if round_number == 1:
            return self.initial_choices(player_reputations)
        choices = ['s' if food_earned_last >= 0 else 'h' for food_earned_last in self.food_earnings]
        return choices[0:len(player_reputations)]

    def hunt_outcomes(self, food_earnings):
        '''Required function defined in the rules'''
        self.total_food_earnings += sum(food_earnings)
        self.food_earnings = food_earnings

    def round_end(self, award, m, number_hunters):
        '''Required function defined in the rules'''
        pass

class ReversePsychologyHunter(BasePlayer):
    '''Slack with players of highest reps and lowest reps, hunt with players of medium rep
    Keep reputation within top 10%
    '''
    def __init__(self):
        super(ReversePsychologyHunter, self).__init__()
        self.name = 'ReversePsychologyHunter'

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
        sorted_reps = sorted(player_reputations, reverse=True)

        ideal_rep = sorted_reps[int(0.3 * len(player_reputations))]

        hunts_needed = self.get_num_hunts_needed(current_reputation, ideal_rep,
                                                 len(player_reputations))
        slacks_needed = len(player_reputations)-hunts_needed

        # print 'sorted', sorted_reps, 'idx', int(0.1 * len(player_reputations)), 'ideal:', ideal_rep, 'hunts needed:', hunts_needed, 'curr_rep', current_reputation

        if round_number == 1:
            return self.initial_choices(player_reputations)

        if hunts_needed < 1 or len(player_reputations) < 3:
            return ['s']*len(player_reputations)

        n_highest_reputations = heapq.nlargest(slacks_needed, player_reputations)
        choices = ['h'] *len(player_reputations)
        for rep in n_highest_reputations:
            player_to_slack_with = player_reputations.index(rep)
            
            choices[player_to_slack_with] = 's'

        return choices

class BoundedHunter(BasePlayer):
    '''Player that hunts whenever the other's reputation is within some range.'''
    def __init__(self,lower,upper):
        self.name = "BoundedHunter" + str(lower)+'-'+str(upper)
        self.low = lower
        self.up = upper

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        return ['h' if self.low <= rep <= self.up else 's' for rep in player_reputations]
        
class AverageHunter(BasePlayer):
    '''Player that tries to maintain the average reputation, but spreads its hunts randomly.'''
    
    def __init__(self):
        self.name = "AverageHunter"

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        avg_rep = sum(player_reputations) / float(len(player_reputations))
        return ['h' if random.random() < avg_rep else 's' for rep in player_reputations]

class TitForTat(BasePlayer):
    def __init__(self):
        """
        Only difference between TitForTat and Player.Player is that this class will 
        titForTat until there's only 2 players left, whereas Player will until 3.
        """
        # Run the inherited class' __init__
        super(TitForTat, self).__init__()
        self.name = 'TitForTat'
        
        # Keep track of these from the previous round
        self.reps_last = []
        self.choices_last = []
        self.results_last = []


    def most_likely_last_index(self, curr_rep):
        ''' Return the index of the reps_last array that contains the last_rep 
        closest to curr_rep
        '''
        return min(range(len(self.reps_last)), key=lambda i: abs(self.reps_last[i]-curr_rep))

    def make_decision(self, my_choice, food_earnings):
        ''' Make a tit-for-tat decision based on the outcome from the previous
        round.  Given the choice my_choice from the last round, and the food earnings
        we can determine what the other player's action was, and use that as our action
        for this round.
        '''
        
        if 'h' == my_choice:
            # If I hunted last round
            # If they hunted, food_earnings will be 0
            return 'h' if food_earnings==0 else 's'        
        else:
            # Otherwise I must have slacked
            # If they hunted, food_earnings will be 1
            return 'h' if food_earnings==1 else 's'

    def calculate_choice(self, partner_rep):
        ''' Calculate whether to hunt or slack based on partner_rep, the current reputation
        of my partner
        '''
        
        # Position of partner in the last round
        idx_last_round = self.most_likely_last_index(partner_rep)

        # my choice last round at idx_last_round and the food_earnings from it
        my_choice_last = self.choices_last[idx_last_round]
        food_earnings_last = self.results_last[idx_last_round]

        # DEBUG
        # if partner_rep == 0:
        #     print 'partner rep', partner_rep
        #     print 'idx', idx_last_round
        #     print 'choice', my_choice_last
        #     print 'earnings',food_earnings_last
        #     print 'reps last', self.reps_last
        #     print 'choices last', self.choices_last
        #     print 'results last', self.results_last

        return self.make_decision(my_choice_last, food_earnings_last)

    # All the other functions are the same as with the non object oriented setting (but they
    # should be instance methods so don't forget to add 'self' as an extra first argument).
    def hunt_choices(self, round_number, current_food, current_reputation, m,
            player_reputations):

        choices = []
        if len(player_reputations) < 2: 
            # Always slack if it's down to three players or less
            choices = ['s']*len(player_reputations)
        elif round_number < 3:
            # Always hunt the first round if there's more than 3 players
            choices = ['h']*len(player_reputations)
        else:
            # Otherwise, hunt using a probabilistic tit-for-tat strategy
            # which matches reps to the closest value from the array of
            # self.reps_last to determine who most likely did what the last round
            for rep in player_reputations:
                choices.append(self.calculate_choice(rep))

        # Save my choices and the player_reputations for next round
        self.choices_last = list(choices)
        self.reps_last = list(player_reputations)
        return choices

    def hunt_outcomes(self, food_earnings):
        self.results_last = list(food_earnings)

    def round_end(self, award, m, number_hunters):
        pass
