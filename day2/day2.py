#data types

#strings
print(len("lol"))
#subscript
print("Hello"[4])
#float 
print(3.14)
#boolean
print(True)

#type conversion & type errors
num_char = 5
print(type(num_char))
new_num = str(num_char)
print(type(new_num))

a = float(123)
print(a)

#Exercise 1
#two_digit_number = input("Type a two digit number: ")
#print(int(two_digit_number[0]) + int(two_digit_number[1]))

#mathematical operations -> PEMDAS
print (2**2) #exponent

#Exercise 2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

float_height = float(height)
int_weight = int(weight)

BMI = (int_weight/(float_height**2))
int_BMI = int(BMI)

print(f"{int_weight} / ({float_height} x {float_height} = {BMI}")
print(f"Rounded down to: {int_BMI}") # floor division //

#Exercise 3
age = input("What is your current age?")
int_age = int(age)
years_left = 90-int_age
print(f"You have {years_left*365} days, {years_left*52} weeks, or {years_left*12} months left to live.")

