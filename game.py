
from player import HumanPlayer , RandomComputerPlayer , GeniusComputerPlayer
import time 

class TicTacToe:
    def __init__(self):
        self.board  = [' ' for _ in range(9)] 
        # we will use it to represent a 3x3 boerd 
        self.current_winner = None # to keep tracking the winner
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| '+' | '.join(row) + ' |')
    
    def avilibal_moves(self):
        return [i for i , spot in enumerate(self.board) if spot == ' ']
        # this 👆is replace of all of that👇
        # moves =[]
        # for i , spot in enumerate(self.board):
        #     # ['x','x','o'] -->    [(0 , 'x'),(1 , 'x'), (2  ,'o')]
        #     if spot == ' ':
        #         moves.append(i)
        #     return moves
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        # return len(self.avilibal_moves())
        return self.board.count(' ')

    def make_move(self ,square , letter ):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter 
            return True
        return False 
    
    def winner(self , square , letter):
        # check the row 
        row_index = square // 3 
        row = self.board[row_index*3:(row_index + 1)*3]
        if all([spot == letter for spot in row]):
            return True
        # check colume 
        colume_index = square % 3 
        colume = [self.board[colume_index+i*3] for i in range(3)]
        if all([spot == letter for spot in colume]):
            return True 
        # check diagonals 
        if square % 2  == 0: 
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True 

            diagonal2 = [self.board[i] for i in [2,4,6]]        
            if all([spot == letter for spot in diagonal2]):
                return True 
        # if there is no winner 
        return False
    


def play(game , x_player , o_player , print_game=True):
    if print_game:
        game.print_board_nums()
    
    letter = 'X' 

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else :
            square = x_player.get_move(game)

        if game.make_move(square , letter):
            if print_game:
                print(f"{letter} makes a move to {square}.")
                game.print_board()
                print('') # just empty line 

                if game.current_winner :
                    if print_game:
                        print(f"{letter} wins!")
                    return letter
                    
                letter = 'O' if letter == 'X' else 'X' 
                # other wat to write an if statement 👆
                if print_game:
                    time.sleep(0.7)

    if print_game: 
        print("it's a tie!")


if __name__ == '__main__':
    x_player =  HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    # o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t , x_player, o_player,print_game=True)
