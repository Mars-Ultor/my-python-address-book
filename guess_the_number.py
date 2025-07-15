import random
secret_number = random.randint(1, 20)
attempts = 0
max_attempts = 4

print("Welcome to Guess the Number!")
print(f"I'm thinking of a number between 1 and 20. You have {max_attempts} attempts to guess")

while attempts < max_attempts:
    try:
        guess = int(input("Take a guess: "))
        attempts += 1
        if guess == secret_number:
            print(f"Congrats! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Your guess is too low. Try again.")
        else:
          print("Your guess is too high. Try again.")
    except ValueError:
        print("Invalid imput. Please enter a whole number.")

else:
    print(f"Sorry, you've used all your attempts. The numer was {secret_number}.")
print("Thanks for playing!")

