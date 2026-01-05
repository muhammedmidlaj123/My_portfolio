students = [
    {"name": "ali", "score": 85},
    {"name": "sara", "score": 92}
]



def calculate_average(student_list):
    total=0
    for student in student_list:
        total += student["score"]

    return total / len(student_list)


while True:
    user_choice = input("Menu: [1] Add, [2] Search, [3] Average, [4] Exit: ")
    if user_choice == "1":
        new_name=input("enter the new new name ")
        new_score=int(input("enter the new score "))
        new_student = {"name": new_name, "score": new_score}
        students.append(new_student)
        print("student added successfully")
    elif user_choice == "2":
        search_name = input("enter the search name ")
        found=False
        for student in students:

            if student["name"] == search_name:
                print(f"student name: {student['score']}")

                if not found:
                    print("Student not found.")
                break
    elif user_choice == "3":
        average = calculate_average(students)

        print(f"average score: {average}")

    else:
        print("exited thankyou !")
        break