username = input("Enter your username: ")
password = input("Enter your password: ")

# Make sure the file name is correct (users.txt vs user.txt)
with open("users.txt", "r") as file:
    lines = file.readlines()  # <--- PLURAL! Get ALL lines.

granted = False

for line in lines:
    clean_line = line.strip()  # Remove \n
    data = clean_line.split(",")  # <--- COMMA! Cut at the comma.

    # SAFETY CHECK: Ensure the line actually has 2 parts before grabbing data
    if len(data) == 2:
        saved_data = data[0]
        saved_pass = data[1]

        # COMPARE INPUT vs SAVED DATA (Not 'lines')
        if username == saved_data and password == saved_pass:
            print("Access Granted")
            granted = True
            break

if not granted:
    print("Access Denied")
