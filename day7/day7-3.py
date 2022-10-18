#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 5

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the lett
# ers in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.


while "_" in display and lives > 0:

    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            print(str(display))
            guess=1
        else:
            guess=0
    if guess == 0:
        lives -=1

if lives > 0:
    print(display + " you have won")
else:
    print("you lose")