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
        pass

