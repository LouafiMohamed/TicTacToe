import math
import random


class player :
    def  __init__(self,letter):
        #letter  x or o 
        self.letter =  letter 
    
    def get_move (self ,game ):
        pass
    

class RandomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self,game):
        square = random.choice(game.avilibal_moves())
        return square

class HumanPlayer(player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self,game):
        valid_squar =False 
        val = None 
        while not valid_squar:
            square = input(f"{self.letter}'s turn. Input move (0-8): ")

            # we are going to check that this is the correct correct value by trying 
            # to cast it to an integer ,and if it's not, then we say it's invalid 
            # if that spot is not avilibal on the board ,we also say it's invalid
             
            try:
                val = int(square)
                if val not in game.avilibal_moves():
                    raise ValueError
                valid_squar = True  
            except ValueError:
                print('Invalid square, plz try again.')
        return val

class GeniusComputerPlayer(player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        if len(game.avilibal_moves()) == 9:
            square = random.choice(game.avilibal_moves()) # just randomly choose at the begening 
        else :
            # get the square based on the minimax algorithme 
            square = self.mimimax(game,self.letter)['position']
        return square
    
    def mimimax(self , state , player):
        max_player = self.letter  
        other_player = 'O' if player == 'X' else 'X' 
        # first we have to check if the privieus move is a winner 
        # this is our base case 
        if state.current_winner == other_player:
            # we should return position AND score because we need to keep tracking for mimimax to work 
            return {'position' : None ,
                'score' : 1*(state.num_empty_squares() + 1 ) if other_player == max_player else (-1*(
                    state.num_empty_squares() + 1 )) 
                    }
        elif not state.empty_squares():
            return {'position' : None ,'score' : 0}
        
        if player == max_player:
            best = {'position' : None ,'score' : -math.inf} # each score is gonna be larger 
        else: 
            best = {'position' : None ,'score' : math.inf} # each score is gonna be smaller  

        for possibale_move in state.avilibal_moves():
            # step 1 : make a move , try that spot 
            state.make_move(possibale_move,player)
            # step 2 : recurse using minimax to similate the game after making that move 
            sim_score = self.mimimax(state,other_player)
            # step 3 : undo that move 
            state.board[possibale_move] = ' '
            state.current_winner = None 
            sim_score['position'] = possibale_move # otherwise this is gonna messed up for the recursion 

            # step 4 : update dictionary if nicecary 
            if player == max_player: # maximize the max player 
                if sim_score['score'] > best['score']:
                    best = sim_score # change best (replace)
            elif player != max_player: # and minimize the other player 
                if sim_score['score'] < best['score']:
                    best = sim_score # change best (replace)
        return best 