import random
import string

def generate_password(length):

    # Набори символів
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Гарантуємо наявність хоча б одного символу кожного типу
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Додаємо випадкові символи до досягнення потрібної довжини
    all_characters = lower + upper + digits + special
    password += random.choices(all_characters, k=length - 4)

    # Перемішуємо символи для випадковості
    random.shuffle(password)

    return ''.join(password)

# Приклад використання
if __name__ == "__main__":
    length = 0
    while length < 4:
        length = int(input("Введіть довжину пароля (не менше 4): "))
    password = generate_password(length)
    print("Згенерований пароль:", password)
    