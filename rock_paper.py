# rock paper scissor game
import random
options=["rock","paper","scissors"]
is_running=True
while is_running:
    computer=random.choice(options)
    player=input("enter your choice:")
    if player not in options:
        print("please enter valid choice")
    else:
        if player==computer:
            print("both are tie")
        elif player=="rock" and computer=="scissors":
            print("you win")
        elif player=="paper" and computer=="rock":
            print("you win")
        elif player=="scissors" and computer=="paper":
            print("you win")
        else:
            print("you lose")
        print(f"computer choice  {computer}")
        wish=input("want to play again ? (y/n)").lower()
        if not wish=="y":
            is_running=False
    

