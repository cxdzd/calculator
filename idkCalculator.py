def calculate(a, op, b):
    a, b = float(a), float(b)
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/": return a / b
    return "Unknown operator"

while True:
    equation = input("Enter equation (or 'quit'): ")
    if equation.lower() == "quit":
        break
    try:
        parts = equation.split()
        if len(parts) == 3:
            a, op, b = parts
            print("Result:", calculate(a, op, b))
        else:
            print("Use format: number operator number (like 2 + 3)")
    except Exception as e:
        print("Error:", e)
