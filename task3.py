print("Illya, IT-31")

first_number = float(input("Enter the first number (float): "))
operator = input("Enter an operation (+, -, *, /, //, %, **): ").strip()
second_number = float(input("Enter the second number (float): "))

valid_operation = True
result = 0.0

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number == 0:
        print(f"Error: division by zero is not allowed.")
        valid_operation = False
    else:
        result = first_number / second_number
elif operator == "//":
    if second_number == 0:
        print(f"Error: division by zero is not allowed.")
        valid_operation = False
    else:
        result = first_number // second_number
elif operator == "%":
    if second_number == 0:
        print(f"Error: division by zero is not allowed.")
        valid_operation = False
    else:
        result = first_number % second_number
elif operator == "**":
    result = first_number ** second_number
else:
    print(f"Error: unknown operation.")
    valid_operation = False

if valid_operation:
    print(f"{first_number} {operator} {second_number} = {result:.4f}")
