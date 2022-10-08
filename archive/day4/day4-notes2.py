fruits = ["apples", "oranges"]
print (fruits)
vegetables = ["beets", "kale"]
print (vegetables)
food = [fruits, vegetables]
new_food = food[0]
new_food[1] = "blueberries"
print (food)










row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column =  int(position[0])
print(column)
row = int(position[1])
print(row)

selected_row = map[column - 1]
print(selected_row)
selected_row[row -1] = "X"





print(f"{row1}\n{row2}\n{row3}")