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

height = float(input("What is your height in m?  "))
weight = float(input("What is your weight in kg?  "))

bmi = round(weight/(height**2))


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

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
else:
    print(f"Your bmi is {bmi}, you are overweight")



   