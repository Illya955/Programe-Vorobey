print("Illya, IT-31")

score = int(input("Enter your score (integer 0-100): "))

if score < 0 or score > 100:
    print(f"Error: score must be between 0 and 100.")
else:
    missed = int(input("Enter missed classes (integer): "))

    if score >= 90:
        grade = "A"
    elif score >= 82:
        grade = "B"
    elif score >= 74:
        grade = "C"
    elif score >= 64:
        grade = "D"
    elif score >= 60:
        grade = "E"
    else:
        grade = "F"

    if missed > 16 * 0.3:
        print(f"Warning: admission is not allowed.")

    if score >= 60 and missed <= 16 * 0.3:
        status = "passed"
    else:
        status = "failed"

    print(f"Score: {score}, Grade: {grade}, Result: {status}")
