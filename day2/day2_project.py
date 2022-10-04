from unicodedata import decimal


print("Welcome to the tip calculator.")
total = float(input("What was the total bill?"))
str_percent = input("What percentage tip would you like to give? 10, 12, or 15?")
str__percent = "1."+str_percent
float_percent = float(str__percent)
int_people = int(input("How many people are splitting the bill?"))
splittotal = round(total*float_percent/int_people,2)
print(f"Each person should pay: {splittotal}")


