import random # You need this at the top

secret_number = random.randint(1, 10)
guess = 0 # This variable will hold the user's guess

# The loop continues as long as the guess is not correct
while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low. Try again!")
    elif guess > secret_number:
        print("Too high. Try again!")
    else:
        print("You guessed it! The number was " + str(secret_number) + "!")
        # The loop will end here because 'guess' is now equal to 'secret_number'