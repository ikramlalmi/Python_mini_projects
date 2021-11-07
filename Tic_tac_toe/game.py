from player import HumanPlayer, RandomComputerPlayer
import time


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # a list for the 3*3 board
        self.current_winner = None
    
    def print_board(self):
        # this is to get a print out of the box
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + "|". join(row)+ "|")
    
    @staticmethod
    def print_board_nums():
        # we want to print 1|2|3 etc, it will tell us what num correspond to what box
        number_board= [[str(i)for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print("|" + "|".join(row) + "|")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # ['x','x','o']->(0,'x'), (1,'x'),(2,'o')
        # for i, spot in enumerate(self.board):
        #     if spot == " ":
        #         moves.append(i)
        # return moves

    def empty_square(self):
        return " " in self.board
    
    def num_empty_square(self):
        return self.board.count(" ")

    def make_move (self, square, letter):
        # if valid move return True, else return false.
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner will have all 3 everywhere,
        # check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1) * 3]
        if all ([spot == letter for spot in row]):
            return True
        
        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range (3)]
        if all ([spot == letter for spot in column]):
            return True

        # check diagonals, only if the square is an even number, these are the only moves to win a diagonal

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] #left to right diagonal
            if all ([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        # if all the checks fail, we dont have a winner, return false
        return False
            


def play(game, x_player, o_player, print_game = True):
    # retruns the winner of the game if there is one and if there isn't return none.
    if print_game:
        game.print_board_nums()

    letter = "X" #starting letter
    # iterterate while the game still has empty spaces.
    
    while game.empty_square():
        if letter == "O":
            # ask the o player to get the move
            square = o_player.get_move(game)
        else:
            # if it is not o, then ask the x player the make a move.
            square = x_player.get_move(game)
        
        # make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes move to square {square}')
                game.print_board()
                print(' ')

            if game.current_winner:
                if print_game:
                    print(letter + " won!")
                return letter

            # switching players
            letter = 'O' if letter == 'X' else 'X'

            # if letter == 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'
        # tiny break
            time.sleep(0.8)

    if print_game:
            print("it is a tie! ")



if __name__ == '__main__':
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, print_game = True)

    