'''
Number Guessing Game
- Random number between 1 and 100
- Tells user if their guess is too high, too low, or correct
'''

import random

num = random.randint(1, 100)
tries = 0

while True:
    user_num = int(input("Guess the number (1-100): "))
    tries += 1

    if user_num == num:
        print(f"Correct! You guessed it in {tries} tries. The number was {num}.")
        break
    elif user_num < num:
        print("Too low!")
    else:
        print("Too high!")
