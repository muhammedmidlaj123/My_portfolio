import random
secret_number=random.randint(1,100)
attempts=0
try:
    with open("highscore.txt","r") as files:
        content=files.read()
        high_score = int(content)
        print(f"Current record: {high_score}")
except FileNotFoundError:
    high_score=100
    print("your the first player")
except ValueError:
    high_score=100
    print("the starting data")


while True:
    try:
        user_input = int(input("Please enter your choice btwm 0-100:   "))
        attempts += 1
        if user_input == secret_number:
            print("your guessed number is correct")
            break
        elif user_input < secret_number:
            print("your guessed number is too low")

        elif user_input > secret_number:
            print("your guessed number is too high")



    except ValueError:
                print("enter a number not text")

if attempts<high_score:
    print("New High Score!")
    with open ("highscore.txt","w") as file:
        file.write(str(attempts))
else:
    print("you didnt break the record")