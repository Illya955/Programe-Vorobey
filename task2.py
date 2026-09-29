
grades_text = "95, 88, 100, 73, 81"
subjects_text = "Programming, Mathematics, English, Physics, History"

grades = [int(x.strip()) for x in grades_text.split(",")]

average = sum(grades) / len(grades)

print(f"Середня оцінка: {average:.2f}")

print("Найвища оцінка:", max(grades))
print("Найнижча оцінка:", min(grades))

grades_joined = " | ".join(str(grade) for grade in grades)

print("Оцінки:", grades_joined)

subjects = [subject.strip()
            for subject in subjects_text.split(",")]

print()
print(f"{'№':<5}{'Предмет':<20}{'Оцінка':>10}")
print("-" * 35)

for number, (subject, grade) in enumerate(
        zip(subjects, grades), start=1):

    print(f"{number:<5}{subject:<20}{grade:>10}")

longest_subject = max(subjects, key=len)

print()
print("Найдовший предмет:", longest_subject)
print("Кількість символів:", len(longest_subject))
