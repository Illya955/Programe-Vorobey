def get_personal_data():
    name = "illya"
    surname = "vorobey"
    group = "it-31"
    return name, surname, group


def create_subjects():
    return [
        ("Programming", 3, 11),
        ("Mathematics", 2, 9),
        ("English", 2, 10),
        ("Computer Networks", 2, 8),
        ("Web Development", 3, 12)
    ]


def print_table(subjects):
    print("#  Subject              Pairs  Grade")

    for number, (title, pairs, grade) in enumerate(subjects, start=1):
        print(f"{number:<3}{title:<21}{pairs:<7}{grade}")


def total_pairs(subjects):
    return sum(pairs for _, pairs, _ in subjects)


def find_most_pairs(subjects):
    return max(subjects, key=lambda subject: subject[1])


def find_weakest(subjects):
    return min(subjects, key=lambda subject: subject[2])


def print_statistics(subjects):
    titles = [title for title, _, _ in subjects]
    grades = [grade for _, _, grade in subjects]

    average = sum(grades) / len(grades)

    print("Titles:", titles)
    print("Grades:", grades, f", average: {average:.2f}")

    high_grades = [title for title, _, grade in subjects if grade >= 10]
    print("Grade 10+:", high_grades)


def print_histogram(subjects):
    for title, _, grade in subjects:
        print(f"{title}: {'#' * grade}")


def retake_weakest(subjects):
    weakest = find_weakest(subjects)
    weakest_title = weakest[0]
    old_grade = weakest[2]
    new_grade = min(old_grade + 2, 12)

    updated_subjects = []

    for title, pairs, grade in subjects:
        if title == weakest_title:
            updated_subjects.append((title, pairs, new_grade))
        else:
            updated_subjects.append((title, pairs, grade))

    print(f"Retake: {weakest_title} {old_grade} -> {new_grade}")

    return updated_subjects


def main():
    name, surname, group = get_personal_data()
    subjects = create_subjects()

    print(f"{name.capitalize()} {surname.capitalize()}, {group}")

    print_table(subjects)

    print("Pairs per week:", total_pairs(subjects))

    most_pairs = find_most_pairs(subjects)
    print(f"Most pairs: {most_pairs[0]} ({most_pairs[1]})")

    weakest = find_weakest(subjects)
    print(f"Weakest subject: {weakest[0]} ({weakest[2]})")

    print_statistics(subjects)

    print_histogram(subjects)

    subjects = retake_weakest(subjects)

    print("Subjects:", subjects)


main()
