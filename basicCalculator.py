while True:
    num1 = input("First number: ")
    num2 = input("Second number")
    
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    op = int(input("Which operation (1/2/3/4): "))

    if op == 1:
        print(num1 + num2)
        break
    elif op == 2:
        print(num1 - num2)
        break
    elif op == 3:
        print(num1 * num2)
        break
    elif op == 4:
        print(num1 / num2)
        break
    else:
        print("Invalid, try agian")