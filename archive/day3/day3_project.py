print("Welcome to Treausre Island.\n Your mission is to find the treasure.")
lorr = input("Do you go left or right? (left/right)   \n")
if lorr == "right":
    print("Game Over. :(")
else:
    swimwait = input("Do you swim across the river or wait?  (swim/wait) \n")
    if swimwait == "swim":
        print("Game Over. :(")
    else:
        door = input("Which door do you choose? Red, Yellow, or Blue? (red/yellow/blue")
        if door == "yellow":
            print("You win!")
        else: 
            print("Game Over. :(")