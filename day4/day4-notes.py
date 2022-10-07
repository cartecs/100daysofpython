import random
import my_module

ran_int = random.randint(0,1)
print (ran_int)

if ran_int == 1:
    print("Heads!")
else:
    print("Tails!")

print(my_module.pi)

ranfloat  = random.random() * 5.1
print (ranfloat)

fruits = ["apples", "oranges", "blueberries"]

# print(fruits[0])
# for i in fruits:
#     print(i)

fruits.append("plum")

# print(fruits[0])
# for i in fruits:
#     print(i)

food = []
food.append(fruits)

print(food)

names = input("Enter some names yo  \n")
list = names.split(", ")
list_num = len(list)
ran_int = random.randint(0,list_num -1)
print(f"{list[ran_int]} pays the bill.")