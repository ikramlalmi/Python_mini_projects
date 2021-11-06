#Guess The number game
import random


def guess(x):
    random_number = random.randint(1 , x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Make a guess for a number between 1 and {x}: "))
        print(guess)
        if guess>random_number:
            print(f"Your guess is too hight!")
        elif guess<random_number:
            print(f"Your guess is too low")
    print(f"Yay! You have guessed right! {random_number}")

# guess(10)

def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        if low != high:
            computer_guess = random.randint(low , high)
        else:
            computer_guess = low

        feedback = input(f"Is the number {computer_guess} too high (H), too low (L), or correct (C): ").lower()
        if feedback == "h":
            high = computer_guess - 1
        if feedback == "l":
            low = computer_guess + 1

    print(f"Yay! you have guessed the right number {computer_guess}!")

# computer_guess(1000)
