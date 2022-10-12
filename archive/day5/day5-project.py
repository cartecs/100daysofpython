#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

let = 0 
num = 1
sym = 2
total = nr_letters + nr_symbols + nr_numbers
run_total=0
run_total_let = 0
run_total_sym = 0
run_total_num = 0
password = []

#password = random combination of letters[x], numbers[x], and symbols[x]

while run_total < total:
    x = random.randint(0,2)
    if x == 0 and run_total_let < nr_letters:
        y=random.randint(0,51)
        password.append(letters[y])
        run_total_let +=1
        run_total +=1
    elif x == 1 and run_total_num < nr_numbers:
        y=random.randint(0,9)
        password.append(numbers[y])
        run_total_num +=1
        run_total+=1
    elif x ==2 and run_total_sym < nr_symbols:
        y=random.randint(0,8)
        password.append(symbols[y])
        run_total_sym +=1
        run_total+=1

print(''.join(password))

    