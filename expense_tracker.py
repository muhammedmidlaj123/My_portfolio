import datetime


class Expense:
    def __init__(self, name, category, amount, date):
        self.name = name
        self.category = category
        self.amount = amount
        self.date = date

    # FIX 1: Merged into ONE single, clean display method
    def __str__(self):
        return f"[{self.date}] {self.name} | {self.category} | ${self.amount}"


class Manager:
    def __init__(self):
        self.expenses = []

    def add_expenses(self, expense):
        self.expenses.append(expense)
        print(f"✅ Added Expense: {expense.name}")

    def save_expenses(self):
        with open("expenses.txt", "w") as file:
            for e in self.expenses:
                # FIX 2: Removed the extra space before the comma
                file.write(f"{e.name},{e.category},{e.amount},{e.date}\n")
        print("💾 Data saved to file.")

    def load_expenses(self):
        try:
            with open("expenses.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")

                    # We extract 4 items now
                    name = data[0]
                    category = data[1]
                    amount = int(data[2])
                    date = data[3]

                    loaded_expense = Expense(name, category, amount, date)
                    self.add_expenses(loaded_expense)

        except FileNotFoundError:
            print("📝 No save file found. Creating a new one...")
        except IndexError:
            print("⚠️ Error: Old file format detected. Please delete expenses.txt.")

    def calculate_total(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        print(f"\n💰 Total Expenses: ${total}")


def main():
    manager = Manager()
    manager.load_expenses()

    # Optional: Show total on startup
    # manager.calculate_total()

    while True:
        print("\n--- 📅 DATED EXPENSE TRACKER ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total")
        print("4. Save & Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name of expense: ")
            category = input("Category: ")
            amount = int(input("Amount: "))

            # Get today's date automatically
            date = datetime.datetime.now().strftime("%Y-%m-%d")

            new_expense = Expense(name, category, amount, date)
            manager.add_expenses(new_expense)

        elif choice == "2":
            print("\n--- Your Expenses ---")
            for item in manager.expenses:
                print(item)

        elif choice == "3":
            manager.calculate_total()

        elif choice == "4":
            manager.save_expenses()
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()