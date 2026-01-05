import random
import time
try:
   with open ("banking.txt", "r") as file:
    text_data = file.read()
    balance = float(text_data)
    print(f"the balance is {balance}")

except FileNotFoundError:
    balance=0
    print("acount is created")
    with open ("banking.txt","w") as file:
        file.writelines("0")
except ValueError:
    balance=0
    print("file was correpted this is new file")
while True:
    menu=input("[1] Deposit, [2] Withdraw, [3] Check Balance, [4] Exit")
    print('processing......')
    time.sleep(1)
    if menu=="1":
        deposit=int(input("Enter the deposit amount: "))
        balance = balance + deposit
        with open ("banking.txt","w") as file:
            file.write(str(balance))
            print("deposit amount has been added")
    elif menu=="2":

        try:
            withdraw = int(input("Enter the withdraw amount: "))
            if withdraw>balance:
               print("You don't have enough money")
            else:
                balance=balance-withdraw
                print(f"The balance is {balance}")

                with open ("banking.txt","w") as file:
                    file.write(str(balance))

        except ValueError:
            print("You don't have enough money")

    elif menu=="3":
        print(f"your balance is {balance}")

    elif menu=="4":
        print("thank you for using midlaj's banking ")
        break









