class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # a list for the 3*3 board
        self.current_winner = None
    
    def print_board(self):
        # this is to get a print out of the box
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + "|". join(row)+"|")
    
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

def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()

    letter = "X" #starting letter
    # iterterate while the game still has empty spaces.
    
    while game.empty_square():
        if letter == "o":
            # ask the o player to get the move
            square = o_player.get_move(game)
        else:
            # ask the x player the make a move.
            square = x_player.get_move(game)
        
        
        # make a move

    