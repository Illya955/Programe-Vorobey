def read_grade(prompt):
    """Read and return a valid grade from 0 to 100."""
    while True:
        value = input(prompt)

        if not value.isdigit():
            print("Error: digits only")
            continue

        grade = int(value)

        if grade < 0 or grade > 100:
            print("Error: the value must be between 0 and 100")
            continue

        return grade


def to_letter(grade):
    """Convert a numeric grade to a letter grade."""
    if grade >= 90:
        return "A"

    if grade >= 82:
        return "B"

    if grade >= 74:
        return "C"

    if grade >= 64:
        return "D"

    if grade >= 60:
        return "E"

    return "F"


def average(grades):
    """Return the arithmetic mean of the grades."""
    return sum(grades) / len(grades)


def count_above(grades, limit):
    """Return the number of grades greater than the limit."""
    count = 0

    for grade in grades:
        if grade > limit:
            count += 1

    return count


def print_report(name, group, grades):
    """Print the student's grade report."""
    avg = average(grades)
    letter = to_letter(avg)
    above = count_above(grades, avg)

    print("--- Report ---")
    print(f"Student: {name}, group {group}")
    print("Grades:", *grades)
    print(f"Average: {avg:.2f} -> {letter}")
    print(f"Best: {max(grades)}, worst: {min(grades)}")
    print(f"Above average: {above}")


def main():
    """Read five grades and print the student's report."""
    name = "Illya"
    surname = "Vorobey"
    group = "IT-31"
    n = len(name)

    print(f"{name} {surname}, {group}")

    grades = []

    for i in range(1, n + 1):
        grade = read_grade(f"Grade {i} (0-100): ")
        grades.append(grade)

    print_report(f"{name} {surname}", group, grades)


main()
