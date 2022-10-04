#exercise 1: print text to console
b = "Hello!"
a = "World!"
print("Hello World!")
print (b + " " + a)

#exercise 3: count letters in input for a name
""" print ("What is your name?")
test = input(b)
number = len([ele for ele in test if ele.isalpha()])
print ("Your name is ",number," letters long") """

#exercise 4: swap a to b and b to a
a = 3
b = 5
temp = a 
a = b 
b = temp 
print ("a: ",a)
print ("b: ",b)

#exercise 5: band name generator
print("Welcome to the band name generator")

city = input("What city did you grow up in?\n")
pet_name = input("What is the name of a pet?\n")
print("Your band name is: " + city + " " + pet_name)