import random

def roll_dice():
    num_1 = random.randint(1, 6)
    num_2 = random.randint(1, 6)
    return num_1 + num_2
wallet=100
result = roll_dice()
print(f"score= {result}")
if result >=8:
    wallet += 10
    print(f"You win!  wallet={wallet} ")


elif result <8:
    wallet -= 10
    print(f"You lose! wallet={wallet}")