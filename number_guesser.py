import random

def number_guesser():
    print("Welcome to the Number Guesser game!")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess the secret number (between 1 and 100): "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guesser()
