
about = "I study Python at college and I enjoy creating useful programs."
day = 5
my_name = "Illya"

words = about.split()

print("Кількість слів:", len(words))

longest_word = max(words, key=len)

print("Найдовше слово:", longest_word)

print("Зворотний порядок:",
      " ".join(words[::-1]))

a_count = about.lower().count("a")

print("Кількість літер 'a':", a_count)

print("З великої літери:",
      about.title())

print("Пробіли замінені на _:",
      about.replace(" ", "_"))


def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


print("Моє ім'я є паліндромом:",
      is_palindrome(my_name))

print('"Never odd or even" є паліндромом:',
      is_palindrome("Never odd or even"))


def caesar_encrypt(text, shift):
    result = ""

    for char in text:

        if char.isalpha():

            base = ord("A") if char.isupper() else ord("a")

            result += chr(
                (ord(char) - base + shift) % 26 + base
            )

        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


encrypted = caesar_encrypt(my_name, day)

decrypted = caesar_decrypt(encrypted, day)

print()
print("Ім'я:", my_name)
print("День народження (зсув):", day)
print("Зашифроване ім'я:", encrypted)
print("Розшифроване ім'я:", decrypted)
