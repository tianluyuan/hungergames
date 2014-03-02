# This file is intended to be a final submission. python tester.py Player.py
# should work at all times. If it does not, there is a bug.

class Player:
    def __init__(self):
        """
        Optional __init__ method is run once when your Player object is created before the
        game starts

        You can add other internal (instance) variables here at your discretion.

        You don't need to define food or reputation as instance variables, since the host
        will never use them. The host will keep track of your food and reputation for you
        as well, and return it through hunt_choices.
        """
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
            # Always slack if it's down to two players
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
