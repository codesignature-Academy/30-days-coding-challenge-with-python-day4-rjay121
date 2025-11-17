choice = "yes"

while choice == "yes":
    print("Welcome to the calculator program")
    print("choose an option")
    print("A. Addition")
    print("B. Subtraction")
    print("C. Mutiplication")
    print("D. Division")

    # get the user option
    option = input("========").upper()

    # get the numbers
    num1 = float(input("Enter your first number"))
    num2 = float(input("Enter your second number"))

    if option == "A":
        solution = num1 + num2
        print(f"The sum of {num1} and {num2} is {solution}")
    elif option == "B":
        solution = num1 - num2
        print(f"The difference of {num1} and {num2} is {solution}")
    elif option == "C":
        solution = num1 * num2
        print(f"The product of {num1} and {num2} is {solution}")
    elif option == "D":
        solution = num1 / num2
        print(f"The division of {num1} and {num2} is {solution}")
    else:
        print("Invalid option")

        choice = input("Do you want to continue? yes or no==")

        if choice not in ["yes", "no"]:
            print("Invalid choice.(must be 'yes' or 'no')")
            break
        print("Existing the calculator program....bye bye")