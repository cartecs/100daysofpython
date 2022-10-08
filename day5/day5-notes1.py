fruits = ["apple", "blueberry"]
for fruit in fruits:
    print(fruit)

total=0
student_heights = 0
i=0
#exercise 1 
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  total += student_heights[n]
  i+=1

avg = total / i
print(avg)