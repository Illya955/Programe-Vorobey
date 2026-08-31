print("Illya, IT-31")

day = int(input("Enter the day (integer): "))
month = int(input("Enter the month (integer 1-12): "))
year = int(input("Enter the year (positive integer): "))

if year <= 0:
    print(f"Date is invalid: year must be positive")
elif month < 1 or month > 12:
    print(f"Date is invalid: month must be between 1 and 12")
else:
    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            max_days = 29
        else:
            max_days = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_days = 30
    else:
        max_days = 31

    if day < 1:
        print(f"Date is invalid: day must be at least 1")
    elif day > max_days:
        print(f"Date is invalid: month {month} has only {max_days} days")
    else:
        print(f"Date is valid")
