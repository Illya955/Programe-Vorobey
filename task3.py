name = "Illya"
surname = "Vorobey"
group = "IT-31"
c = len(surname)


def get_initials(name: str, surname: str) -> str:
    """Return initials of a name and surname."""
    return f"{name[0].upper()}.{surname[0].upper()}."


def count_letters(text: str, letter: str = "a") -> int:
    """Return how many times letter occurs in text."""
    count = 0

    for char in text.lower():
        if char == letter.lower():
            count += 1

    return count


def count_vowels(text: str) -> int:
    """Return the number of vowels in text."""
    vowels = "aeiouy"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count


def reverse_text(text: str) -> str:
    """Return text in reverse order without slicing."""
    result = ""

    for char in text:
        result = char + result

    return result


print(f"{name} {surname}, {group}")
print(f"Initials: {get_initials(name, surname)}")

print(f"Letters in surname: {c}")

vowels = count_vowels(surname)
consonants = c - vowels

print(f"Vowels: {vowels}, consonants: {consonants}")

for vowel in "aeiou":
    amount = count_letters(surname, letter=vowel)
    print(f"{vowel}: {amount}")

print(f"Default letter 'a': {count_letters(surname)}")

print(f"Reversed surname: {reverse_text(surname)}")

print(f"Docstring: {count_letters.__doc__}")
print(f"Annotations: {count_letters.__annotations__}")
