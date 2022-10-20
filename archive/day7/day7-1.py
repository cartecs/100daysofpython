#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

word= random.randint(0,2)
chosen_word = word_list[word]
#choice 

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = (input("Guess a letter:  \n")).lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for l in chosen_word:
    if guess == l:
        print("This letter is in the word")
    else:
        print("This letter is not in the word")