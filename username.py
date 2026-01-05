print("****calculator***")
num1=float(input("enter your first number:"))
num2=float(input("enter your second number:"))

print("enter 1 for 'addition' \n enter 2 for 'subraction'\n enter 3 for 'multiplication'\n enter 4 for 'division'")
Entered_number = int(input("choice a number from 1 to 4:"))

if Entered_number ==1:
    print("addition of your first and second number is :",num1+num2)

elif Entered_number == 2:
    print("subraction of your first and second number is :", num1 - num2)
elif Entered_number ==3:
    print("multilplication  of your first and second number is :", num1 * num2)
elif Entered_number == 4:
    print("division  of your first and second number is :", num1 / num2)
else :
      print ("syntax error")

