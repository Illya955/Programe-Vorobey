# Task 1 - Vorobey - It21

birth_day = 5
height_meters = 1.82
full_name = "Illia Vorobey"
scholarship = False

print(f"birth_day = {birth_day}, type = {type(birth_day)}")
print(f"height_meters = {height_meters}, type = {type(height_meters)}")
print(f"full_name = {full_name}, type = {type(full_name)}")
print(f"gets_scholarship = {scholarship}, type = {type(scholarship)}")

print(f"Before change: birth_day = {birth_day}, type = {type(birth_day)}")
print(f"Before change: scholarship = {scholarship}, type = {type(scholarship)}")

birth_day = "five"
scholarship = 0.0

print(f"After change: birth_day = {birth_day}, type = {type(birth_day)}")
print(f"After change: gets_scholarship = {scholarship}, type = {type(scholarship)}")

try:
    result = birth_day + 1
    print(f"Result = {result}")
except TypeError as error:
    print(f"Error: {error}")
