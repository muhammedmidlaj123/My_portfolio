# --- 1. THE LOGIC ---
class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"✅ {self.name}, new balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("👎 Insufficient balance!")
        else:
            self.balance -= amount
            print(f"✅ Withdrawn! Remaining: {self.balance}")


# --- 2. THE OBJECT ---
# Create the account BEFORE the loop starts
my_acc = Account("Sam")

# --- 3. THE INTERFACE ---
while True:
    print("\n1. Deposit | 2. Withdraw | 3. Check Balance | 4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        amt = int(input("Amount to deposit: "))
        # call the deposit function on my_acc
        my_acc.deposit(amt)

    elif choice == "2":
        amt = int(input("Amount to withdraw: "))
        # ⚠️ YOUR TURN: Call the withdraw function on my_acc
        my_acc.withdraw(amt)

    elif choice == "3":
        # ⚠️ YOUR TURN: Print my_acc.balance
        print(f"Your balance is: {my_acc.balance}")

    elif choice == "4":
        break