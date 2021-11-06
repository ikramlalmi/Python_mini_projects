import random
from words import words
import string
from hangmen_visual import lives_visual_dic


def get_valid_word(words):
    word = random.choice(words)
    while " " in word and "-" in word: #only get a word that does not have a space of a dash
        word = random.choice(words)
    return word.upper()


def hangmen():    
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word to be guessed
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7
    


    while len(word_letters) > 0 and lives > 0 :
        print(lives_visual_dic[lives])
        #the current word is : w - o - d
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("the current word:", " ".join(word_list))
        print("you have ", lives, "lives left and you have used these letters so far:", " ".join(used_letters))
        user_letter = input("type something: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else :
                lives-=1
                print(f"the letter is not in the word!, you have lost a life, you have {lives} left")
               
                
        elif user_letter in used_letters:
            print('you have already used that letter before, try again!')
        else:
            print("invalid input, try again")
    # you will exit the loop if they won or if they die
    if lives==0:
        print("sorry, you died!, the word was ", word)
    else: 
        print(f"you have guessed the word : {word} !")

 

if __name__ == '__main__' :
    hangmen()