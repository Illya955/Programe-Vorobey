name = "Illya"
surname = "Vorobey"
group = "IT-31"
y = 2008


def print_age(year):
    """Print the age and return nothing."""
    age = 2026 - year
    print(f"Age: {age}")


def get_age(year, current_year=2026):
    """Return the age for the specified current year."""
    if year > current_year or year < 0:
        return -1

    age = current_year - year
    return age

    print("after return")


print(f"{name} {surname}, {group}")

print_age(y)

result = print_age(y)
print(f"print_age returned: {result}")

age = get_age(y)
print(f"Age from get_age: {age}")

print(f"Age in months: {age * 12}")
print(f"Age in weeks: {age * 52}")

age_2030 = get_age(y, current_year=2030)
print(f"Age in 2030: {age_2030}")

print(f"Invalid year 3000 gives: {get_age(3000)}")
