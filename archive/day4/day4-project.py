import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))

choices = [rock, paper, scissors]

print("Your choice:  \n" + choices[choice])

computer = random.randint(0,2)

print("Your opponent chooses: \n" + choices[computer])

if choice == 0 and computer == 2:
    print("You win!")
elif choice == 2 and computer == 0:
    print("You lose!")
elif choice > computer:
    print("you win!")
elif choice < computer:
    print("you lose!")
elif choice == computer:
    print ("you tied!")
    




#rock
# 0 > 2
# 0 = 0
# 0 < 1

#paper
# 1 > 0 
# 1 =1
# 1 < 2

#scissor
#2 < 0 
#2 > 1 
# 2 = 2
