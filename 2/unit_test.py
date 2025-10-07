import unittest
import string
from unittest.mock import patch

from main import generate_password  

class TestPasswordGenerator(unittest.TestCase):

    def test_password_length(self):
        # Перевіряє, що пароль має правильну довжину
        for length in [4, 8, 12, 16]:
            with self.subTest(length=length):
                password = generate_password(length)
                self.assertEqual(len(password), length)

    def test_password_contains_lowercase(self):
        # Перевіряє, що пароль містить хоча б одну малу літеру
        password = generate_password(8)
        self.assertTrue(any(c in string.ascii_lowercase for c in password))

    def test_password_contains_uppercase(self):
        # Перевіряє, що пароль містить хоча б одну велику літеру
        password = generate_password(8)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))

    def test_password_contains_digits(self):
        # Перевіряє, що пароль містить хоча б одну цифру
        password = generate_password(8)
        self.assertTrue(any(c in string.digits for c in password))

    def test_password_contains_special_chars(self):
        # Перевіряє, що пароль містить хоча б один спеціальний символ
        password = generate_password(8)
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_password_all_required_chars_present(self):
        # Перевіряє, що всі обов'язкові типи символів присутні в паролі
        password = generate_password(8)
        
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_special = any(c in string.punctuation for c in password)
        
        self.assertTrue(has_lower, "Не знайдено малих літер")
        self.assertTrue(has_upper, "Не знайдено великих літер")
        self.assertTrue(has_digit, "Не знайдено цифр")
        self.assertTrue(has_special, "Не знайдено спеціальних символів")

    def test_password_randomness(self):
        # Перевіряє, що згенеровані паролі різні (випадковість)
        passwords = [generate_password(8) for _ in range(5)]
        # Перевіряємо, що хоча б деякі паролі різні
        self.assertTrue(len(set(passwords)) > 1, "Паролі недостатньо випадкові")

    def test_password_characters_from_valid_set(self):
        # Перевіряє, що всі символи пароля з допустимого набору
        password = generate_password(10)
        valid_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        for char in password:
            self.assertIn(char, valid_chars, f"Неприпустимий символ '{char}' в паролі")

    def test_multiple_passwords_different(self):
        # Перевіряє, що кілька згенерованих паролів різні
        passwords = [generate_password(12) for _ in range(10)]
        unique_passwords = set(passwords)
        
        # Очікуємо, що більшість паролів будуть унікальними (допускаємо випадкові дублікати)
        self.assertGreaterEqual(len(unique_passwords), 8, 
                               "Згенеровано занадто багато однакових паролів")

if __name__ == "__main__":
    unittest.main()