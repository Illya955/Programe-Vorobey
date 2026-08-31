print("Illya Vorobey, IT-31")

name = input("Enter your name (text): ").strip()

if not name:
    print(f"The name was not entered")
    name = "Anonymous"

age = int(input("Enter your age (integer): "))

if age < 0:
    category = "invalid value"
elif age <= 6:
    category = "child"
elif age <= 17:
    category = "schoolchild"
elif age <= 64:
    category = "adult"
else:
    category = "senior"

print(f"Hello, {name}! Your age category is {category}.")
