from words import words
import random
import string


# def print_letter(user_letter):
#     if user_letter == "E":
#         for x in num_lines["E"]:     
#                 print(x)
#     elif user_letter == "F":
#          for x in num_lines["F"]:
#                 print(x)
#     else :print ("Sorry! Invalid charachter! ")


# def print_mood(user_mood):
#     if user_mood == "H":
#         print (user_moods["Happy"])
#     elif user_mood == "S":
#         print (user_moods["Sad"])
#     elif user_mood == "G":
#         print (user_moods["Gangster"])
#     else:print ("invalid mood")


# num_lines =  { 
#     "F":( "---------", "|", "|", "---------","|", "|"),"E": ( "---------", "|", "|", "---------","|", "|","---------")
# }

# user_moods = {
#     "Happy" : "😁",
#     "Sad" : "😣" ,
#     "Gangster" : "😎"
# }

# # letter = input("which letter would you like to see printed in the terminal 'F' or 'E' :")
# # mood = input ("What is your current mood? 'H' for 'happy' or 'S' for 'Sad, 'G' for 'Gangster''" )
# # print_letter(letter.upper())
# # print_mood (mood.upper())
# # -------------------------------------
def random_word(words):
    # if we end up with an invalid word from the list keep looking
    word = random.choice(words)
    while " " in word and "-" in word:
       word = random.choice(words) 
    return word.upper()

def hangmen():
    word = random_word(words)
    # turn it in a random word into a set of letters
    word_letter = set(word)
    # the list of letters that had been used are stored in the used_letters set
    used_letters = set()
    # needs to compare to the english alphabet all in uppercase
    alphabet = set(string.ascii_uppercase)
    # since we will keep removing letter from word letter as the user guesses righ
    # we wil keep asking for input until the condition is met, we will remove the letter from the word letter as the user gueeses right
   
    while len(word_letter)>0:
        #print w - r d
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("the word : ", " ".join(word_list))
        print("letters used so far: ", " ".join(used_letters))
        # ask the user for a letter input and store it in the user letter set 
        user_letter = input("type a letter :").upper()
        # we want to make sure it has not been used beofer, so we will compare it to the alphabet 
        if user_letter in alphabet - used_letters: 
            used_letters.add(user_letter)
            if user_letter in word_letter:
                    word_letter.remove(user_letter)
                    
        elif user_letter in used_letters:
                print("you have already used this letter!")

        else: print("invalid charachter!")

    print(f"Yay! you have guessed the word {word} right!")

hangmen()
