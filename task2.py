print("Illya, IT-31")

number = int(input("Enter an integer: "))

if number > 0:
    sign = "positive"
elif number < 0:
    sign = "negative"
else:
    sign = "zero"

print(f"The number is {sign}")

if number != 0:
    if number % 2 == 0:
        parity = "even"
    else:
        parity = "odd"

    print(f"The number is {parity}")

    if 10 <= abs(number) <= 99:
        print(f"The number is two-digit")
