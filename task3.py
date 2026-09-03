print("Illya Vorobey, IT-31")

name = "Illya"
surname = "Vorobey"

full_name = name + surname
vowels = 0
consonants = 0

for char in full_name:
    if char.lower() in "aeiouy":
        vowels += 1
    else:
        consonants += 1

print(f"Vowels: {vowels}, consonants: {consonants}")
print(f"Total letters: {len(full_name)}")
