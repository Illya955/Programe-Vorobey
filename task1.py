name = "Illya"
surname = "Vorobey"
group = "IT-31"
year = 2008


def print_card():
    """Print the student's personal information."""
    print(f"Name: {name} {surname}")
    print(f"Group: {group}")
    print(f"Birth year: {year}")


def print_card_args(name, surname, group=group, year=year):
    """Print personal information using function parameters."""
    print(f"{name} {surname}, {group}, {year}")


print(f"{name} {surname}, {group}")

print("--- no parameters, call 1 ---")
print_card()

print("--- no parameters, call 2 ---")
print_card()

print("--- no parameters, call 3 ---")
print_card()

print("--- positional arguments ---")
print_card_args("Illya", "Vorobey", "IT-31", 2008)

print("--- keyword arguments ---")
print_card_args(year=2008, group="IT-31",
                surname="Vorobey", name="Illya")

print("--- mixed arguments ---")
print_card_args("Illya", "Vorobey", group="IT-31", year=2008)

print("--- default group ---")
print_card_args("Illya", "Vorobey", year=2008)
