import unittest
import os
import tempfile
from main import VernamCipher  # Замість 'vernam_cipher' вкажи ім'я твого файлу

class TestVernamCipher(unittest.TestCase):
    
    def setUp(self):
        # Створюємо тимчасову папку для тестів
        self.test_dir = tempfile.mkdtemp()
        self.cipher = VernamCipher(self.test_dir)
    
    def tearDown(self):
        # Видаляємо тимчасову папку після тестів
        import shutil
        shutil.rmtree(self.test_dir)
    
    def test_encrypt_decrypt_ukrainian_text(self):
        # Тест шифрування та дешифрування українського тексту
        original_text = "Привіт Україна! Це тест шифрування."
        encrypted, key = self.cipher.encrypt(original_text)
        decrypted_text = self.cipher.decrypt(encrypted, key)
        self.assertEqual(original_text, decrypted_text)
    
    def test_encrypt_decrypt_english_text(self):
        # Тест шифрування та дешифрування англійського тексту
        original_text = "Hello World! This is a test."
        encrypted, key = self.cipher.encrypt(original_text)
        decrypted_text = self.cipher.decrypt(encrypted, key)
        self.assertEqual(original_text, decrypted_text)
    
    def test_encrypt_decrypt_special_characters(self):
        # Тест шифрування тексту з спеціальними символами
        original_text = "Test 123! @#$%^&*()"
        encrypted, key = self.cipher.encrypt(original_text)
        decrypted_text = self.cipher.decrypt(encrypted, key)
        self.assertEqual(original_text, decrypted_text)
    
    def test_encrypt_decrypt_empty_string(self):
        # Тест шифрування порожнього рядка
        original_text = ""
        encrypted, key = self.cipher.encrypt(original_text)
        decrypted_text = self.cipher.decrypt(encrypted, key)
        self.assertEqual(original_text, decrypted_text)
    
    def test_encrypt_decrypt_long_text(self):
        # Тест шифрування довгого тексту
        original_text = "Це дуже довгий текст для перевірки роботи шифрування. " * 10
        encrypted, key = self.cipher.encrypt(original_text)
        decrypted_text = self.cipher.decrypt(encrypted, key)
        self.assertEqual(original_text, decrypted_text)
    
    def test_key_length_matches_text(self):
        # Тест що довжина ключа дорівнює довжині тексту
        test_text = "Test message"
        encrypted, key = self.cipher.encrypt(test_text)
        self.assertEqual(len(test_text.encode('utf-8')), len(key))
    
    def test_different_keys_for_same_text(self):
        # Тест що для одного тексту генеруються різні ключі
        test_text = "Same text"
        encrypted1, key1 = self.cipher.encrypt(test_text)
        encrypted2, key2 = self.cipher.encrypt(test_text)
        self.assertNotEqual(key1, key2)
        self.assertNotEqual(encrypted1, encrypted2)
    
    def test_decrypt_with_wrong_key_fails(self):
        # Тест що дешифрування з неправильним ключем не працює
        original_text = "Secret message"
        encrypted, correct_key = self.cipher.encrypt(original_text)
        
        # Генеруємо неправильний ключ
        wrong_key = self.cipher.generate_key(len(correct_key))
        
        # Спробуємо дешифрувати з неправильним ключем
        with self.assertRaises(UnicodeDecodeError):
            self.cipher.decrypt(encrypted, wrong_key)
    
    def test_save_to_file_bytes(self):
        # Тест збереження байтів у файл
        test_data = b"test binary data"
        filepath = self.cipher.save_to_file("test.bin", test_data)
        self.assertTrue(os.path.exists(filepath))
        
        # Перевіряємо вміст файлу
        with open(filepath, 'rb') as f:
            content = f.read()
        self.assertEqual(test_data, content)
    
    def test_save_to_file_text(self):
        # Тест збереження тексту у файл
        test_text = "Тестовий текст"
        filepath = self.cipher.save_to_file("test.txt", test_text)
        self.assertTrue(os.path.exists(filepath))
        
        # Перевіряємо вміст файлу
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertEqual(test_text, content)
    
        

if __name__ == "__main__":
    # Запуск тестів
    unittest.main()