import random


def play():
    user = input("What is your choice: 'r' for rock, 'p' for paper and 's' for scissors\n")
    computer = random.choice(['r', 'p', 'r'])
    if user == computer :
        return "it is a tie!"
    
    if is_win(user, computer):
        return "Your won!"

    return "Your lost!"




# r>s, s>p, p>r
def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

print(play())