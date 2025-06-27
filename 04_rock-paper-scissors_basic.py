# Choose (rock/paper/scissors): rock  
# Computer chose: scissors  
# You win! 🎉

import random
#define choice
choices = ["rock", "paper", "scissors"]
#user choice 
user = input("Choose (rock/paper/scissors) :").lower()
#generate computer choice
computer = random.choice(choices)
print(f"Computer Chose : {computer}" )

if user == computer:
    print("It's a tie")

elif (
    (user == "rock" and computer == "scissors") or
    (user == "paper" and computer == "rock") or
    (user == "scissors" and computer == "paper")
):
    print("You win! 🎉")
else :
    
    print("You lose 😢")




