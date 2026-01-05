user_name=input("enter your name:   ")
user_number=input("enter your number:   ")
with open("contacts.txt", "a") as file:
    file.write(f"{user_name},{user_number}\n")


print("saved")

while True:
    user_input=input("[1] Add Contact, [2] Search Contact, [3] Exit")
    if user_input == "1":
        user_name1=input("enter the name:   ")
        user_number1=input("enter the number:   ")
        with open("contacts.txt", "a") as file:
            file.write(f"{user_name1},{user_number1}\n")

    elif user_input == "2":


            target_name = input("enter target name")
            found = False

            with open("contacts.txt", "r") as file:
                lines = file.readlines()

            for line in lines:
                clean_lines = line.strip()
                data = clean_lines.split(",")

                if data[0] == target_name:
                     print(f"Found Number: {data[1]}")
                     found = True
                     break
            if not found:
                    print("Not Found:")

    if user_input == "3":
        print("goodbye")
        break
