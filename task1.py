name = "illya"
surname = "vorobey"
group = "it-31"

grades = [10, 8, 8, 9, 8, 10, 9]

print("Grades:", grades)
print("Count:", len(grades))
print("Sum:", sum(grades))
print("Best grade:", max(grades))
print("Worst grade:", min(grades))
print("Average:", f"{sum(grades) / len(grades):.2f}")

sorted_grades = sorted(grades, reverse=True)
print("Sorted grades:", sorted_grades)
print("Original grades:", grades)

print("Top 3:", sorted(grades, reverse=True)[:3])
print("Bottom 3:", sorted(grades)[:3])

worst_grade = min(grades)
print("Position of worst grade:", grades.index(worst_grade) + 1)

average = sum(grades) / len(grades)
above_average = [grade for grade in grades if grade > average]
print("Above average:", above_average)
print("Count above average:", len(above_average))

print("Has 12:", 12 in grades)
print("Has 1:", 1 in grades)

grades.append(len(surname) % 12 + 1)
print("After adding c % 12 + 1:", grades)

grades.insert(0, 12)
print("After inserting 12 at beginning:", grades)

grades.remove(min(grades))
print("After removing worst grade:", grades)

removed_grade = grades.pop()
print("Removed last grade:", removed_grade)
print("After removing last grade:", grades)

print("Number of 12s:", grades.count(12))

result = grades.sort()
print("Return value of sort():", result)
print("Grades after sort:", grades)