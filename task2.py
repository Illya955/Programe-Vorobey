print("Illya Vorobey, IT-31")

number = int(input("Enter an integer: "))

if number <= 0:
    if number == 0:
        print("Digits: 1")
        print("Sum of digits: 0")
        print("Max digit: 0, min digit: 0")
        print("Reversed: 0")
    else:
        number = abs(number)

        digits = 0
        digit_sum = 0
        max_digit = 0
        min_digit = 9
        reversed_number = 0

        while number > 0:
            digit = number % 10
            digits += 1
            digit_sum += digit

            if digit > max_digit:
                max_digit = digit

            if digit < min_digit:
                min_digit = digit

            reversed_number = reversed_number * 10 + digit
            number //= 10

        print(f"Digits: {digits}")
        print(f"Sum of digits: {digit_sum}")
        print(f"Max digit: {max_digit}, min digit: {min_digit}")
        print(f"Reversed: {reversed_number}")
else:
    digits = 0
    digit_sum = 0
    max_digit = 0
    min_digit = 9
    reversed_number = 0

    while number > 0:
        digit = number % 10
        digits += 1
        digit_sum += digit

        if digit > max_digit:
            max_digit = digit

        if digit < min_digit:
            min_digit = digit

        reversed_number = reversed_number * 10 + digit
        number //= 10

    print(f"Digits: {digits}")
    print(f"Sum of digits: {digit_sum}")
    print(f"Max digit: {max_digit}, min digit: {min_digit}")
    print(f"Reversed: {reversed_number}")
