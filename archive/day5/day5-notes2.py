#exercise 2
student_scores = input("Input a list of student scores ").split()
highest_score = 0
for n in range(0, len(student_scores)): #range steps through from 0 to x -- in this case length of students
  student_scores[n] = int(student_scores[n])
  if student_scores[n] > highest_score:
    highest_score = student_scores[n]

print(student_scores)
print(highest_score)

# total=0
# for number in range(1,101):
#     total+=number
# print(total)

even_numbers = 0
numbers = input("Input a list of numbers ").split()
for n in range(0, len(numbers)):
    numbers[n] = int(numbers[n])
    if numbers[n] % 2 == 0:
        print(numbers[n])
        #even_numbers.append(numbers[n])
        even_numbers += numbers[n]

print(even_numbers)


for number in range(1,101):
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
            print("Buzz")
    elif number % 3 == 0:
            print("Fizz")
    else:
        print(number)



