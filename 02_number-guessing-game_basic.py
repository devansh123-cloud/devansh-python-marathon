#import and secret function
import random
secret = random.randint(1, 10)
tries = 0
print("I'm thinking of a number between 1 and 10...")
#while , try , except function use
while True:
    try:
        guess = int(input("Your Guess :"))
    except ValueError:
        print("❌ Please enter a number, not letters!")
        continue

    tries += 1
    #use of if/else operator
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {tries} tries. 🏆")
        break
    