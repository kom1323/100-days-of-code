import random
import hangman_art
import hangman_words
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



stages1 = hangman_art.stages
end_of_game = False
lives = 6
curr_stage = 5
display = []
used_words = []
guess = " "
in_word_flag = True


word = random.choice(hangman_words.word_list)
word_length = len(word)

for letter in word:
    display.append("_")


while not end_of_game:


    print(hangman_art.logo)
    print("The chosen word is: " + word)
    print(f"{' '.join(display)}")
    print(stages1[lives])
    if not in_word_flag:
        print(f"The letter '{guess}' is not in the word. You lost a life.")
    guess = input("Guess a letter: ")
    clearConsole()


    while guess in used_words:
       print(hangman_art.logo)
       print("The chosen word is: " + word)
       print(f"{' '.join(display)}")
       print(stages1[lives])
       print("You already guessed " + guess)
       guess = input("Guess a letter: ")
       clearConsole()

    else:
      used_words.append(guess)
      
    
    in_word_flag = False
    for position in range(word_length):
        letter = word[position]
        if letter == guess:
            display[position] = letter
            in_word_flag = True

    if not in_word_flag:
      lives -= 1
    
    if lives == 0:
        end_of_game = True
        clearConsole
        print(hangman_art.logo)
        print(f"{' '.join(display)}")
        print(stages1[lives])
        print("You lost")

    if "_" not in display:
        end_of_game = True
        clearConsole()
        print(hangman_art.logo)
        print(f"{' '.join(display)}")
        print(stages1[lives])
        print("You Win")



    
    
