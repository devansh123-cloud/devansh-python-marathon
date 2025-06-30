import random

print("🎲 Welcome to Number Guessing Game!")

while True:
    secret = random.randint(1, 20)
    tries = 0
    print("\nI'm thinking of a number between 1 and 20...")

    while True:
        try:
            guess = int(input("Your Guess: "))
        except ValueError:
            print("❌ Please enter a number, not letters!")
            continue

        tries += 1

        if guess < secret:
            print("Too low! ⬇️")
        elif guess > secret:
            print("Too high! ⬆️")
        else:
            print(f"🎉 Correct! You guessed it in {tries} tries.")
            break  # guess was correct → break inner loop

    # after the correct guess, ask if they want to play again
    user_input = input("Wanna play again? (yes/no): ").lower()
    if user_input == "yes":
        continue
    
    elif user_input == "no":
        print("Thanks for Playing")
        break
