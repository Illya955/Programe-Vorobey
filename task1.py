me = {
    "name": "Illya",
    "surname": "Vorobey",
    "group": "IT-31",
    "city": "Kovel",
    "birth_year": 2008,
    "hobbies": ["sleep", "eat", "box"]
}

# Виводимо кожну пару ключ -> значення
print("Information about me:")
for key, value in me.items():
    print(key, "->", value)

# Виводимо список ключів і кількість пар
print("\nKeys:", list(me.keys()))
print("Number of pairs:", len(me))

# Виводимо групу
print("\nGroup:", me["group"])

# Безпечне отримання email, якого поки немає
print("Email:", me.get("email", "unknown"))

# me["email"] тут завершило б програму помилкою KeyError,
# тому що такого ключа ще немає у словнику.

# Додаємо навчальну пошту
me["email"] = "vorobey.iv2008@gmail.com"

# Змінюємо місто
me["city"] = "Lutsk"

# Вилучаємо рік народження
removed_year = me.pop("birth_year")
print("\nRemoved birth year:", removed_year)

# Виводимо словник після всіх змін
print("\nDictionary after changes:")
for key, value in me.items():
    print(key, "->", value)

# Перевіряємо наявність ключа phone
print("\nIs 'phone' in dictionary?", "phone" in me)
