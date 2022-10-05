#day 3 of 100 days of python
#conditionals: if & else
""" print("Welcome to the rollercoaster!")
height = int(input("Whatt is your heigh in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print ("You cannot ride the rollercoaster!") """

#exercise 1
""" number = int(input("Which number do you want to check"))

if number % 2 == 0:
    print("Even")
else:
    print ("Odd") """

# height = float(input("What is your height in m?  "))
# weight = float(input("What is your weight in kg?  "))

# bmi = round(weight/(height**2))


# if bmi < 35:
#     if bmi < 18.5:
#         print("You are underweight")
#     else:
#         if bmi < 25:
#             print("normal weight")
#         else:
#             if bmi < 30:
#                 print("overweight")
#             else:
#                 if bmi < 35:
#                     print("obese")
# else:
#     print("clinically obese")

# if bmi < 18.5:
#     print(f"Your bmi is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your bmi is {bmi}, you have a normal weight.")
# else:
#     print(f"Your bmi is {bmi}, you are overweight")

#exercise 3
#on every year that is divisible by 4
#exceptt every year that is evenly disible by 100
#unless the year is also divisible by 400

# year = int(input("Enter a year:   "))

# i=0
# # if year % 4 == 0:
# if year % 4 == 0:
#     i = 1
#     if year % 4 == 0 and year % 100 == 0:
#         i = 0
#         if year % 4== 0 and year % 100 == 0 and year % 400 == 0:
#             i = 1
#         elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
#             i = 0
#     else:
#         y = 0
# else:
#     i = 0
        
# # 200

# if i == 1:
#     print("Leap year")
# else:
#     print ("Not a leap year")



total = 0
print("Welcome to Python Pizza Deliveries!  ")
size = input("What size pizza do you want? S, M, L?  ")
#S $15, M, $20, L, $25
add_pepperoni = input("Do you want pepperoni? yes/no") #$2 for small, $3 for large / med
extra_cheese = input("Do you want extra cheese? yes/no") #$1 

if size == "S":
    total=15
if size == "M":
    total=20
if size == "L":
    total=25

if add_pepperoni == "yes":
    if size == "M" or size == "L":
        total+=3
    else:
        total+=2

if extra_cheese == "yes":
    total+=1

print(f"Your total is: {total}")



