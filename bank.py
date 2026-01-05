import os
import datetime
import google.generativeai as genai
from colorama import Fore, init

# 1. Initialize Colors
init(autoreset=True)

# 2. Security: Ask for API Key at Runtime
key = input(f"{Fore.YELLOW}🔑 Enter your Google API Key to start: ")
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- FILE DATABASE SETTINGS ---
DB_FILE = "users.txt"


# --- HELPER: SAVE & LOAD ---
def load_accounts():
    accounts = []
    if not os.path.exists(DB_FILE):
        return accounts

    with open(DB_FILE, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if len(data) == 3:
                name, password, balance = data
                # Reconstruct the user
                acc = Account(name, password, float(balance))
                accounts.append(acc)
    return accounts


def save_accounts(accounts_list):
    with open(DB_FILE, "w") as f:
        for acc in accounts_list:
            f.write(f"{acc.name},{acc.password},{acc.balance}\n")


# --- AI ADVISOR (GUARDRAILED) ---
def ask_ai_advisor(user_name):
    print(f"\n{Fore.CYAN}🤖 SAM (BANK ONLY) IS ONLINE...")

    while True:
        question = input(f"\n{Fore.WHITE}You: ")
        if question.lower() == "exit":
            print(f"🤖 SAM: Session closed.")
            break

        print(f"{Fore.YELLOW}SAM is analyzing...")
        try:
            prompt = f"""
            SYSTEM: You are SAM, a strict Banking AI for 'Smart Bank'.
            USER: {user_name}
            RULES:
            1. ONLY answer questions about Money, Loans, Interest, Savings, or Investing.
            2. IF the user asks about anything else (movies, coding, life), REJECT IT politely.
            3. Keep answers professional and short.

            QUESTION: {question}
            """
            response = model.generate_content(prompt)
            print(f"\n{Fore.GREEN}💬 SAM: {Fore.WHITE}{response.text}")
        except Exception as e:
            print(f"{Fore.RED}❌ Error: {e}")


# --- CLASS: ACCOUNT ---
class Account:
    def __init__(self, name, password, balance=0.0):
        self.name = name
        self.password = password
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"✅ Deposited ${amount}")
        print(f"{Fore.GREEN}✅ Deposited ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.history.append(f"📉 Withdrew ${amount}")
            print(f"{Fore.CYAN}📉 Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            print(f"{Fore.RED}⚠️ Insufficient Funds!")

    def view_history(self):
        print(f"\n{Fore.YELLOW}--- 📜 TRANSACTION HISTORY ---")
        if not self.history:
            print("No transactions yet (in this session).")
        else:
            for item in self.history:
                print(item)
        print("-" * 30)


# --- CLASS: BANK SYSTEM ---
class BankSystem:
    def __init__(self):
        self.accounts = load_accounts()  # Load data on startup
        self.current_user = None

    def save(self):
        save_accounts(self.accounts)  # Save data to file

    def login(self):
        print(f"\n{Fore.MAGENTA}--- 🔐 LOGIN ---")
        name = input("Username: ").strip().lower()
        password = input("Password: ").strip()

        for acc in self.accounts:
            if acc.name == name and acc.password == password:
                self.current_user = acc
                print(f"{Fore.GREEN}✅ Welcome back, {acc.name.title()}!")
                return True

        print(f"{Fore.RED}❌ Wrong Name or Password.")
        return False

    def signup(self):
        print(f"\n{Fore.MAGENTA}--- 📝 REGISTER ---")
        name = input("Choose Username: ").strip().lower()

        # Check if taken
        for acc in self.accounts:
            if acc.name == name:
                print(f"{Fore.RED}⚠️ User already exists!")
                return

        password = input("Choose Password: ").strip()
        new_acc = Account(name, password)
        self.accounts.append(new_acc)
        self.save()  # Save immediately
        print(f"{Fore.GREEN}✅ Account Created! Please Login.")

    def apply_loan(self):
        print(f"\n{Fore.MAGENTA}--- 💸 LOAN APPLICATION ---")
        amt = float(input("Enter Loan Amount: "))
        years = int(input("Enter Duration (Years): "))

        # 1. Calculate the Interest
        rate = 6.5 if years < 3 else 8.0
        interest = (amt * rate * years) / 100
        total_repay = amt + interest
        emi = total_repay / (years * 12)

        print(f"{Fore.YELLOW}📊 Quote: Interest Rate {rate}%")
        print(f"{Fore.YELLOW}💰 Monthly EMI: ${round(emi, 2)}")
        print(f"{Fore.YELLOW}💵 Total to Repay: ${total_repay}")

        # 2. Ask to Confirm
        confirm = input("\nDo you want to approve this loan? (yes/no): ").lower()

        if confirm == "yes":
            # 3. TRANSFER THE MONEY
            self.current_user.balance += amt

            # 4. UPDATE HISTORY
            # (We manually add this entry to the history list)
            self.current_user.history.append(f"💸 Loan Approved: +${amt}")

            # 5. SAVE TO FILE
            self.save()

            print(f"{Fore.GREEN}✅ Loan Approved! ${amt} has been added to your account.")
            print(f"New Balance: ${self.current_user.balance}")
        else:
            print(f"{Fore.RED}❌ Loan Cancelled.")

    def main_menu(self):
        while True:
            # --- STATE 1: LOGGED OUT (Login Menu) ---
            if self.current_user is None:
                print(f"\n{Fore.MAGENTA}--- 🏦 SMART BANK v2.0 ---")
                print("1. Login")
                print("2. Create New Account")
                print("3. Exit")

                choice = input("Choose: ")

                if choice == "1":
                    self.login()
                elif choice == "2":
                    self.signup()
                elif choice == "3":
                    print("Goodbye!")
                    break

            # --- STATE 2: LOGGED IN (Dashboard) ---
            else:
                print(f"\n{Fore.CYAN}--- 👤 DASHBOARD: {self.current_user.name.upper()} ---")
                print("1. Deposit")
                print("2. Withdraw")
                print(f"3. {Fore.GREEN}Ask SAM (AI)")
                print("4. Apply for Loan")
                print("5. View History")
                print("6. Logout")

                choice = input("Option: ")

                if choice == "1":
                    amt = float(input("Amount: "))
                    self.current_user.deposit(amt)
                    self.save()  # Save changes
                elif choice == "2":
                    amt = float(input("Amount: "))
                    self.current_user.withdraw(amt)
                    self.save()  # Save changes
                elif choice == "3":
                    ask_ai_advisor(self.current_user.name)
                elif choice == "4":
                    self.apply_loan()
                elif choice == "5":
                    self.current_user.view_history()
                elif choice == "6":
                    print(f"🔒 Logging out...")
                    self.current_user = None


if __name__ == "__main__":
    app = BankSystem()
    app.main_menu()