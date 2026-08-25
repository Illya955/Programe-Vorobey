# Task 3 - Vorobey - It21

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print(f"{first_number} + {second_number} = {first_number + second_number}")
print(f"{first_number} - {second_number} = {first_number - second_number}")
print(f"{first_number} * {second_number} = {first_number * second_number}")

if second_number != 0:
    print(f"{first_number} / {second_number} = {first_number / second_number}")
    print(f"{first_number} // {second_number} = {first_number // second_number}")
    print(f"{first_number} % {second_number} = {first_number % second_number}")
else:
    print("Division by zero is not allowed.")

print(f"{first_number} ** {second_number} = {first_number ** second_number}")
