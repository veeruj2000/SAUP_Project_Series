import random
com_win=0
user_win=0
print("Welcome to the Tournament of Rock, Paper, Scissors")
print("Please enter the number of rounds you want to play in a tournament.")
n=int(input("Enter Rounds in Tournament: "))
for i in range(0,n):
    user_action=input("Enter Choice(Rock, Paper, Scissor): ")
    possible_action=["Rock", "Paper", "Scissor"]
    computer_action=random.choice(possible_action)
    print("You choose ", user_action, ", Computer chooses ", computer_action)
    if (computer_action==user_action):
        print("The game is a tie. Both chose ", user_action)
    elif(user_action=="Rock"):
        if (computer_action=="Paper"):
            print("Computer Won!")
            com_win= com_win+1
        else:
            print("Congratulations! You Won")
            user_win = user_win+1
    elif(user_action=="Paper"):
        if(computer_action=="Rock"):
            print("Congratulations! You Won")
            user_win = user_win+1
        else:
            print("Computer Wins!")
            com_win= com_win+1
    elif(user_action=="Scissor"):
        if(computer_action=="Rock"):
            print("Computer Wins!")
            com_win= com_win+1
        else:
            print("Congratulations! You Won")
            user_win = user_win+1
print(f' You won {user_win} times computer won {com_win} times')
if(com_win>user_win):
    print("Computer wins the tournament")
elif(user_win>com_win):
    print("You won the tournament")
else:
    ("The tournament remains on a tie")