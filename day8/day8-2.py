#Write your code below this line 👇
def prime_checker(number):
    #one and itself
    a = []
    f = 2
    while number > 1:
        if number % f == 0:
            a.append(f)
            number //=f
        else:
            f +=1
    return a


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
#print(prime_checker(number=n))
x = len(prime_checker(number=n))
if x > 1:
    print("This number is not prime")
else:
    print("This number is prime")
