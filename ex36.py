from sys import exit
import time
import random


def the_hangman():
    words = ["patronus","gryffin","siren","pegasus","centaur","yeti","minotaur","kraken"]
    special_word = "Loch Ness Monster"

    word_hint = {
        "patronus": "Expecto _______(insert word here)",
        "gryffin": "part Simba, part eagle",
        "siren": "an evil mermaid",
        "pegasus": "a flying horse",
        "centaur": "like when you're riding a horse except you're joined to it",
        "yeti": "It is Abominable.",
        "minotaur": "Can be found in the middle of Labyrnith - and no, not the singer",
    }

    word_of_the_day = random.choice(words)
    print(word_of_the_day)

    separated_word = []
    for letter in word_of_the_day:
        separated_word.append(letter)

    word_length = len(word_of_the_day)
    template = ['_ ' * word_length]
    print(template)
    guessed = []
    tries = 5


    input("You see a distorted face hung to the ceiling.")
    input("Guess the word or you'll end up like me he says.")
    input("Well since you're bored why not?")
    input("\n")

    input("...LOADING...")

    time.sleep(2)
    input("\nYou have 5 tries. \nIf you guess one wrong letter the number, the number of tries you have reduces by 1.")
    input("After 2 tries, you get a hint.")

    
    while tries != 0:
        print(f"You have {tries} tries left.")
        print(f"This is your progress: {template} ")
        guess = input("Guess a letter: ")
        guess = guess.lower()


        if tries == 1:
            print(f"This is your hint: {word_hint[word_of_the_day]}")
        
        if guess in guessed:
            print("You've already guessed it.")
        
        if letter not in separated_word:
            tries -= 1
            input("Oops, wrong guess :( !")
        
        if letter in separated_word:
            guessed.append(guess)
            input("It is in the word. You got this!")
            # if separated_word.count(guess) == 0:
            in_dex = separated_word.index(guess)
            template[in_dex] = guess
        else:
                # in_dices = [i for i, x in enumerate(separated_word) if x == guess]
                # for z in in_dices:
                    # template[z] = guess
            pass

        end_game = input("If you have guessed all the letters, enter True.")     
        if end_game == "True":
            print("Congratulations! You live to see another day!")
            exit(0)
    print("Good job! You're dead. I hope you find death by hanging suitable.")

the_hangman()