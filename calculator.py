#calculator 
num1=int(input("enter first number"))
num2=int(input("enter second number"))
print("choose operation")
print("1-addition")
print("2-subtraction")
print("3-multiplication")
print("4-divide")
choice=input("enter your choice 1|2|3|4")
if choice == "1":
    print("Result:", num1 + num2)

elif choice == "2":
    print("Result:", num1 - num2)

elif choice == "3":
    print("Result:", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("invalid choice")
