import random

# Number Guessing Game

print("===== NUMBER GUESSING GAME =====")

while True:

    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")

    while True:

        guess = int(input("Enter your guess: "))
        attempts = attempts + 1

        if guess < secret_number:
            print("Too Low! Try Again.")

        elif guess > secret_number:
            print("Too High! Try Again.")

        else:
            print("Correct! You Won!")
            print("Total Attempts:", attempts)
            break

    play_again = input("\nDo you want to play again? (yes/no): ")

    if play_again.lower() != "yes":
        print("Thank you for playing!")
        break