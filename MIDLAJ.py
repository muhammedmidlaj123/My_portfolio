import datetime


# --- CLASS 1: THE ROBOT (Account) ---
class Account:
    def __init__(self, owner_name):
        self.owner = owner_name
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.history.append(f"[{date}] Deposited: ${amount}")
        print(f"✅ New Balance: ${self.balance}")

    # This is the MATH method (The Robot Brain)
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            self.history.append(f"[{date}] Withdrew: ${amount}")
            print(f"✅ Withdraw Successful. New Balance: ${self.balance}")
        else:
            print("⚠️ Insufficient Funds!")

    def print_statement(self):
        print(f"\n--- 📜 Statement for {self.owner} ---")
        for item in self.history:
            print(item)
        print(f"💰 Final Balance: ${self.balance}\n")


# --- CLASS 2: THE MANAGER (BankSystem) ---
class BankSystem:
    def __init__(self):
        self.accounts = []

    def find_account(self, name_to_find):
        for account in self.accounts:
            if account.owner == name_to_find:
                return account
        return None

    def create_account(self):
        name = input("Enter your name: ")
        new_account = Account(name)
        self.accounts.append(new_account)
        print(f"✅ Account created for {name}")

    def deposit_money(self):
        name = input("Enter your name: ")
        selected_account = self.find_account(name)
        if selected_account is not None:
            amt = int(input("Enter amount: "))
            selected_account.deposit(amt)
        else:
            print("❌ Account doesn't exist")

    def withdraw_money(self):
        name = input("Enter your name: ")
        selected_account = self.find_account(name)

        if selected_account is not None:
            amt = int(input("Enter amount to withdraw: "))
            # KEY FIX: Actually calling the withdraw method now!
            selected_account.withdraw(amt)
        else:
            print("❌ Account doesn't exist")

    def view_history(self):
        name = input("Enter your name: ")
        selected_account = self.find_account(name)

        if selected_account is not None:
            selected_account.print_statement()
        else:
            print("❌ Account doesn't exist")

    def main_menu(self):
        # The Login Log
        name = input("Enter your name to login: ")
        with open("database.txt", "a") as file:
            file.write(name + "\n")
            print("✅ Login saved to hard drive")

        while True:
            print("\n--- 🏦 BANK MENU ---")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. View History")
            print("5. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit_money()
            elif choice == "3":
                self.withdraw_money()
            elif choice == "4":
                self.view_history()
            elif choice == "5":
                print("Goodbye!")
                break


if __name__ == "__main__":
    app = BankSystem()
    app.main_menu()


