
import random
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
rounds = 3

print("🎮 Rock Paper Scissors – Best of 3\n")
for i in range (1, rounds+1):
    print(f"Round {i}")
    user = input("Choose (rock/paper/scissors:)").lower().strip()

    if user not in choices:
        print("❌ Invalid choice! Please choose rock, paper, or scissors.\n")
        continue
    
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    
    if user == computer:
        print("It's a tie \n")
    
    elif (   
    (user == "rock" and computer == "scissors") or 
    (user == "paper" and computer == "rock") or 
    (user == "scissors" and computer == "paper")
    ):
        print("You win this round 🎉\n")
        user_score += 1
    else:
        print("Computer wins the round 😢\n")
        computer_score += 1
    
    #Final Score Summary
    print("🧮 Final Score:")
    print(f"You : {user_score} | Computer: {computer_score}")
    
    if user_score > computer_score:
        print("You won the game!")
    
    elif computer_score >  user_score:
        print("Computer won the game!")
    
    else:
        print("It's a draw!")
    