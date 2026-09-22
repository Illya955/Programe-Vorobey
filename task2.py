schedule = {
    "Mon": [
        "Programming",
        "Ukrainian Language for Professional Purposes",
        "Administration of Operating Systems and Computer Networks"
    ],
    "Tue": [
        "Programming",
        "IT Law",
        "Databases in Information Systems"
    ],
    "Wed": [
        "Foreign Language for Professional Purposes",
        "Databases in Information Systems",
        "Web Resource Development"
    ],
    "Thu": [
        "Programming",
        "Web Resource Development",
        "Administration of Operating Systems and Computer Networks"
    ],
    "Fri": [
        "Foreign Language for Professional Purposes",
        "Web Resource Development",
        "IT Law"
    ]
}


# Виводимо таблицю розкладу
print("WEEKLY SCHEDULE")
print("-" * 90)
print(f"{'Day':<8} {'Number of classes':<20} Subjects")
print("-" * 90)

for day, subjects in schedule.items():
    print(f"{day:<8} {len(subjects):<20} {', '.join(subjects)}")


# Загальна кількість пар за тиждень
total_classes = sum(len(subjects) for subjects in schedule.values())

print("\nTotal number of classes:", total_classes)


# День із найбільшою кількістю пар
max_day = max(schedule, key=lambda day: len(schedule[day]))

print("Day with the most classes:", max_day)
print("Number of classes:", len(schedule[max_day]))


# Створюємо множину всіх різних предметів
all_subjects = set()

for subjects in schedule.values():
    all_subjects.update(subjects)

print("\nAll unique subjects:")
print(all_subjects)
print("Number of unique subjects:", len(all_subjects))


# Предмети, які є і в понеділок, і в середу
monday_subjects = set(schedule["Mon"])
wednesday_subjects = set(schedule["Wed"])

both_days = monday_subjects & wednesday_subjects

print("\nSubjects on both Monday and Wednesday:")
print(both_days)


# Предмети, які є в понеділок, але немає в середу
monday_only = monday_subjects - wednesday_subjects

print("\nSubjects on Monday but not on Wednesday:")
print(monday_only)


# Функція для підрахунку кількості пар кожного предмета
def count_subjects(schedule):
    subject_counts = {}

    for subjects in schedule.values():
        for subject in subjects:
            subject_counts[subject] = subject_counts.get(subject, 0) + 1

    return subject_counts


# Викликаємо функцію
subject_counts = count_subjects(schedule)

print("\nSubject counts:")
for subject, count in subject_counts.items():
    print(subject, "->", count)


# Сортуємо предмети від найбільшої кількості пар до найменшої
rating = sorted(
    subject_counts.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nSUBJECT RATING")
for number, (subject, count) in enumerate(rating, start=1):
    print(f"{number}. {subject} - {count} classes")
