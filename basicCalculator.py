while True:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    op = int(input("Which operation (1/2/3/4): "))

    if op == 1:
        print(num1 + num2)
    elif op == 2:
        print(num1 - num2)
    elif op == 3:
        print(num1 * num2)
    elif op == 4:
        print(num1 / num2)
    else:
        print("Invalid, try again")