import unittest
import random
# Замініть на правильний імпорт вашого класу Cipher
# from ваш_файл import Cipher

# Тимчасова заглушка для тестування
class Cipher:
    def __init__(self, key):
        self.key = key

    def substitution_encrypt(self, text):
        encrypted = ''.join(chr((ord(char) + self.key) % 256) for char in text)
        return encrypted

    def substitution_decrypt(self, text):
        decrypted = ''.join(chr((ord(char) - self.key) % 256) for char in text)
        return decrypted

    def transposition_encrypt(self, text):
        if len(text) % self.key != 0:
            text = text + ' ' * (self.key - len(text) % self.key)
        encrypted = ''.join(text[i::self.key] for i in range(self.key))
        return encrypted

    def transposition_decrypt(self, text):
        rows = len(text) // self.key
        decrypted = ''.join(text[i::rows] for i in range(rows))
        return decrypted.rstrip()

    def gamma_encrypt(self, text):
        random.seed(self.key)
        gamma = [random.randint(0, 255) for _ in range(len(text))]
        encrypted = ''.join(chr(ord(char) ^ gamma[i]) for i, char in enumerate(text))
        return encrypted

    def gamma_decrypt(self, text):
        random.seed(self.key)
        gamma = [random.randint(0, 255) for _ in range(len(text))]
        decrypted = ''.join(chr(ord(char) ^ gamma[i]) for i, char in enumerate(text))
        return decrypted

    def analytical_transform_encrypt(self, text):
        encrypted = ''.join(chr((ord(char) * self.key) % 256) for char in text)
        return encrypted

    def analytical_transform_decrypt(self, text):
        # Знаходимо обернений елемент за модулем 256
        try:
            inverse_key = pow(self.key, -1, 256)
        except ValueError:
            inverse_key = 1  # Якщо ключ не має оберненого
            
        decrypted = ''.join(chr((ord(char) * inverse_key) % 256) for char in text)
        return decrypted

class TestCipher(unittest.TestCase):
    
    def setUp(self):
        """Ініціалізація перед кожним тестом"""
        self.key = 5
        self.cipher = Cipher(self.key)
        self.test_texts = [
            "Hello, World!",
            "Hello!",
            "1234567890",
            "!@#$%^&*()",
            "Test with spaces",
            "",  # пустий рядок
            "A" * 10  # довгий текст (зменшено для тесту)
        ]
    
    def test_substitution_basic(self):
        """Базовий тест методу заміни"""
        text = "Hello"
        encrypted = self.cipher.substitution_encrypt(text)
        decrypted = self.cipher.substitution_decrypt(encrypted)
        self.assertEqual(text, decrypted)
    
    def test_substitution_various_texts(self):
        """Тест методу заміни з різними текстами"""
        for text in self.test_texts:
            with self.subTest(text=text):
                encrypted = self.cipher.substitution_encrypt(text)
                decrypted = self.cipher.substitution_decrypt(encrypted)
                self.assertEqual(text, decrypted)
    
    def test_transposition_basic(self):
        """Базовий тест методу перестановки"""
        text = "Hello World"
        encrypted = self.cipher.transposition_encrypt(text)
        decrypted = self.cipher.transposition_decrypt(encrypted)
        self.assertEqual(text, decrypted)
    
    def test_gamma_basic(self):
        """Базовий тест гаммування"""
        text = "Secret message"
        encrypted = self.cipher.gamma_encrypt(text)
        decrypted = self.cipher.gamma_decrypt(encrypted)
        self.assertEqual(text, decrypted)
    
    def test_analytical_basic(self):
        """Базовий тест аналітичного перетворення"""
        text = "Test123"
        encrypted = self.cipher.analytical_transform_encrypt(text)
        decrypted = self.cipher.analytical_transform_decrypt(encrypted)
        self.assertEqual(text, decrypted)
    
    def test_empty_string(self):
        """Тест роботи з порожнім рядком"""
        text = ""
        
        # Метод заміни
        encrypted = self.cipher.substitution_encrypt(text)
        decrypted = self.cipher.substitution_decrypt(encrypted)
        self.assertEqual(text, decrypted)
        
        # Метод перестановки
        encrypted = self.cipher.transposition_encrypt(text)
        decrypted = self.cipher.transposition_decrypt(encrypted)
        self.assertEqual(text, decrypted)
        
        # Гаммування
        encrypted = self.cipher.gamma_encrypt(text)
        decrypted = self.cipher.gamma_decrypt(encrypted)
        self.assertEqual(text, decrypted)

if __name__ == "__main__":
    # Запуск без SystemExit помилки
    unittest.main(verbosity=2, exit=False)
    
    