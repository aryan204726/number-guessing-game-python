
# number-guessing-game-python



# Number Guessing Game (Python)

A simple Python console game where the computer picks a random number between 1 and 100, and the player tries to guess it. The game gives hints to guess higher or lower until the player guesses correctly.

## How to play

1. Run the Python script:
   ```bash
   main.py
Enter your guesses when prompted.

The game will guide you by telling you if the guess is too high or too low.

Keep guessing until you find the right number.

The game shows the total number of attempts.

Code features
Random number generation with Python's random module

Input validation to ensure numbers only

Feedback for each guess


Guess the number
Enter the guess = 50
Higher number...
Enter the guess = 75
Lower number..
Enter the guess = 63
You guess the right number in 3 attempts

Made with ❤️ in Python.

---

### 3. `main.py` file content:

```python
import random

# generate the random number between 1 to 100
n = random.randint(1, 100)
guess = None
attempt = 0

print("Guess the number ")

while guess != n:
    try:
        guess = int(input("Enter the guess = "))
        attempt += 1
        
        if guess > n:
            print("Lower number..")
        elif guess < n:
            print("Higher number...")
        else:
            print(f"You guessed the right number in {attempt} attempts!")
    except ValueError:
        print("Enter a valid number please")
