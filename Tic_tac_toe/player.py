import math 
import random

class Player:
    def __init__(self, letter):
        # either going to O or x
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # pass in a random valid spot for the next move using the available move fucntion
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        # to store the value input from the user that is actually valid
        val = None
        while not valid_square:
            square = input(self.letter + "\'s turn. to play. Imput move (0-8): " )
            # check if imput is valid by casting it to an integer,and
            try:
                val = int(square)
                if val not in  game.available_moves():
                    raise ValueError
                valid_square = True # the square in valid
            except ValueError:
                print("Invalid square. try again!")
        return val


