
full_name = " vOROBEY illya vITALIYOVYCH "
group = "IT-31"

parts = full_name.split()
clean_name = " ".join(parts).title()

print("Охайне ім'я:", clean_name)
print("Довжина:", len(clean_name))


surname, name, patronymic = clean_name.split()

print("Перший символ прізвища:", surname[0])
print("Останній символ прізвища:", surname[-1])
print("Прізвище навпаки:", surname[::-1])

print("Ім'я у форматі:", f"{surname} {name[0]}. {patronymic[0]}.")
print("Ініціали:", f"{surname[0]}{name[0]}{patronymic[0]}")

vowels = "aeiou"
vowels_count = sum(1 for char in clean_name.lower() if char in vowels)

print("Кількість голосних:", vowels_count)

dash_position = group.find("-")

print("Частина до дефіса:", group[:dash_position])
print("Частина після дефіса:", group[dash_position + 1:])
print("Частина після дефіса є числом:",
      group[dash_position + 1:].isdigit())

login = f"{name[0].lower()}.{surname.lower()}"
email = f"{login}@student.edu.ua"

print("Логін:", login)
print("Пошта:", email)
