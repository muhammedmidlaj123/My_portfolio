import datetime


class Robort:
    def __init__(self, name, part_name, part_type, price, date):
        self.name = name
        self.part_name = part_name
        self.part_type = part_type
        self.price = price
        self.date = date

    def __str__(self):
        return f"[{self.date}] {self.name} | {self.part_name} ({self.part_type}) | ${self.price}"


class Manager:
    def __init__(self):
        self.inventory = []

    def add_robort(self, robot):
        self.inventory.append(robot)
        print(f"✅ Added: {robot.part_name}")

    def save_inventory(self):
        with open("inventory.txt", "w") as file:
            for item in self.inventory:
                file.write(f"{item.name},{item.part_name},{item.part_type},{item.price},{item.date}\n")
        print("💾 Inventory saved.")

    def load_inventory(self):
        try:
            with open("inventory.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    price = int(data[3])
                    loaded_robot = Robort(data[0], data[1], data[2], price, data[4])
                    self.inventory.append(loaded_robot)
            print("📂 Inventory loaded.")
        except FileNotFoundError:
            print("📝 No inventory file found. Starting fresh.")

    def calculate_value(self):
        total = 0
        for robot in self.inventory:
            total += robot.price
        print(f"\n💰 Total Lab Value: ${total}")

    # --- ✅ CORRECTLY PLACED SEARCH METHOD ---
    def search_component(self, query):
        print(f"\n🔎 Searching for '{query}'...")
        found = False
        for robot in self.inventory:
            # Check if query is inside the part name (case insensitive)
            if query.lower() in robot.part_name.lower():
                print(robot)
                found = True

        if not found:
            print("❌ No matching components found.")

    def delete_robot(self, user_number):
        index = user_number - 1

        # Check if index is INSIDE the list (Valid)
        if 0 <= index < len(self.inventory):
            deleted_item = self.inventory.pop(index)
            print(f"❌ Deleted: {deleted_item.part_name}")

        # If it is OUTSIDE the list (Invalid)
        else:
            print("⚠️ Error: That number does not exist.")




def main():
    manager = Manager()
    manager.load_inventory()

    while True:
        print("\n--- 🤖 ROBOTICS LAB MANAGER ---")
        print("1. Add New Component")
        print("2. List Inventory")
        print("3. Calculate Total Value")
        print("4. Search Inventory")
        print("5. for delete iems ")
        print("6. Save & Exit")  # <--- MOVED TO 5

        choice = input("Select option (1-5): ")

        if choice == "1":
            print("\n--- New Component Details ---")
            name = input("Robot Name (e.g., Optimus): ")
            part = input("Part Name (e.g., Servo): ")
            type_ = input("Part Type (e.g., Motor): ")
            price = int(input("Price ($): "))
            date = datetime.datetime.now().strftime("%Y-%m-%d")

            new_robot = Robort(name, part, type_, price, date)
            manager.add_robort(new_robot)

        elif choice == "2":
            print("\n--- Current Inventory ---")
            count=1
            for item in manager.inventory:

                print(f"{count},{item}")
                count += 1



        elif choice == "3":
            manager.calculate_value()

        # --- NEW SEARCH LOGIC ---
        elif choice == "4":
            search_term = input("What are you looking for? (e.g., Motor): ")
            manager.search_component(search_term)

        elif choice == "5":
            # Show list first so they know the numbers
            count = 1
            for item in manager.inventory:
                print(f"{count}. {item}")
                count += 1

            num = int(input("\nEnter number to delete: "))
            manager.delete_robot(num)


        elif choice == "6":
            manager.save_inventory()
            print("System shutting down... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
