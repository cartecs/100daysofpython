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