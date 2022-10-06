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



# total = 0
# print("Welcome to Python Pizza Deliveries!  ")
# size = input("What size pizza do you want? S, M, L?  ")
# #S $15, M, $20, L, $25
# add_pepperoni = input("Do you want pepperoni? yes/no") #$2 for small, $3 for large / med
# extra_cheese = input("Do you want extra cheese? yes/no") #$1 

# if size == "S":
#     total=15
# if size == "M":
#     total=20
# if size == "L":
#     total=25

# if add_pepperoni == "yes":
#     if size == "M" or size == "L":
#         total+=3
#     else:
#         total+=2

# if extra_cheese == "yes":
#     total+=1

# print(f"Your total is: {total}")



count1 = 0
count2 = 0
name1 = input("What is your name?  \n")
name2 = input ("What is their name? \n")

name1_lower = name1.lower()
name2_lower = name2.lower()
# #true love
# for element_true in range(0, len("true")):
#     for name1_l in range(0, len(name1_lower)):
#         if name1_lower[name1_l] == "true"[element_true]:
#             count1+=1
#     for name2_l in range(0, len(name2_lower)):
#         if name2_lower[name2_l] == "true"[element_true]:
#             count1+=1

# for element_love in range(0, len("love")):
#     for ename1_l in range(0, len(name1_lower)):
#         if name1_lower[name1_l]== "love"[element_love]:
#             count2+=1
#     for name2_l in range(0,len(name2_lower)):
#         if name2_lower[name2_l] == "love"[element_love]:
#             count2+=1

# count1= 0
# count2=0

# n1 = name1_lower
# n2 = name2_lower

# for i, v in enumerate("true"):
#     for x, y in enumerate(n1):
#         if v == y:
#             count1+=1
#     for s, t in enumerate(n2):
#         if v == t:
#             count1+=1

# for q,r in enumerate("love"):
#     for w,u in enumerate(n1):
#         if r ==u:
#             count2+=1
#     for e,f in enumerate(n2):
#         if r == f:
#             count2+=1




# one = str(count1)
# two = str(count2)
# percent = one + two
# int_percent = int(percent)

# if int_percent < 10 or int_percent > 90:
#     print("less than 10 or greater than 90")
# elif int_percent >= 40 or int_percent <= 50:
#     print("less tahn 50 greater than 40")
# else:
#     print (f"your score is {int_percent}")

count_num=0

# blar

string_name = name1_lower
for i,v in enumerate("true"):
    for j,w in enumerate(name1_lower):
        if w == v:
            print(w + " = " + v)
            count_num+=1
        else:
            print(w + "!=" + v)
    for k,x in enumerate(name2_lower):
        if x == v:
            print(x + " = " + v)
            count_num+=1
print(f"true count: {count_num}")
true_count = count_num
count_num = 0

string_name = name2_lower
for i,v in enumerate("love"):
    for j,w in enumerate(name1_lower):
        if w == v:
            print(w + " = " + v)
            count_num+=1
        else:
            print(w + "!=" + v)
    for k,x in enumerate(name2_lower):
        if x == v:
            print(x + " = " + v)
            count_num+=1
print(f"love count: {count_num}")
love_count = count_num


love_string = str(love_count)

true_string = str(true_count)

print(true_string + love_string)

comb_string = true_string + love_string

comb_num = int(comb_string)

print(comb_num)

if comb_num < 10 or comb_num > 90:
    print(comb_num)
elif comb_num  >= 40 and comb_num<= 50:
    print(comb_num)
else:
    print("no")


