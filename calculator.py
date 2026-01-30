print("Calculator")

while True:
    expression = input("What is your equation (or quit with q): ")

    if expression == "q":
        print("Goodbye")
        break

    try:
        answer = eval(expression)
        print("Answer: ", answer)
    except Exception as e:
        print("Invalid equation: ", e)