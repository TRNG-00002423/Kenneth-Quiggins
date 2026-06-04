import random; 

answer = random.randint(1, 100)

max_guesses = 7
guess_count = 0 

while guess_count < max_guesses:

    user_input = input("Guess a number between 1 and 100")

    if not user_input.isdigit():
        print("Please enter a valid number")

    guess = int(user_input)

    guess_count += 1

    remaining = max_guesses - guess_count

    if guess < answer:
        print(f"Too Low")

    elif guess > answer:
        print("Too High")

    else:
        print("You guessed it")
else:
    print("Game over")