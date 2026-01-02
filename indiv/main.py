import os

class VernamCipher:
    def __init__(self, folder="4"):
        self.folder = folder
        os.makedirs(self.folder, exist_ok=True)
    
    def generate_key(self, length):
        # Генерація випадкового ключа такої ж довжини як текст
        return os.urandom(length)
    
    def encrypt(self, text):
        # Перетворення тексту у байти
        text_bytes = text.encode('utf-8')
        
        # Генерація ключа такої ж довжини
        key = self.generate_key(len(text_bytes))
        
        # Побітове XOR між текстом та ключем
        encrypted_bytes = bytes([text_byte ^ key_byte for text_byte, key_byte in zip(text_bytes, key)])
        
        return encrypted_bytes, key
    
    def decrypt(self, encrypted_bytes, key):
        # Побітове XOR між шифротекстом та ключем (та сама операція)
        decrypted_bytes = bytes([enc_byte ^ key_byte for enc_byte, key_byte in zip(encrypted_bytes, key)])
        
        # Перетворення байтів назад у текст
        return decrypted_bytes.decode('utf-8')
    
    def save_to_file(self, filename, data):
        # Збереження даних у файл у папці 4
        filepath = os.path.join(self.folder, filename)
        if isinstance(data, bytes):
            with open(filepath, 'wb') as f:
                f.write(data)
        else:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(data)
        return filepath

def main():
    cipher = VernamCipher("4")
    
    # Оригінальний текст
    original_text = "Привіт! Це тест шифрування Вернама."
    print(f"Оригінальний текст: {original_text}")
    
    # Шифрування
    encrypted, key = cipher.encrypt(original_text)
    print("Текст зашифровано методом Вернама!")
    
    # Дешифрування
    decrypted_text = cipher.decrypt(encrypted, key)
    print(f"Дешифрований текст: {decrypted_text}")
    
    # Перевірка коректності
    print(f"Тексти співпадають: {original_text == decrypted_text}")
    
    # Збереження у файли
    cipher.save_to_file("original.txt", original_text)
    cipher.save_to_file("encrypted.bin", encrypted)
    cipher.save_to_file("key.bin", key)
    cipher.save_to_file("decrypted.txt", decrypted_text)
    
    print(f"\nФайли збережено у папці 4:")
    print("- original.txt - оригінальний текст")
    print("- encrypted.bin - зашифровані дані")
    print("- key.bin - ключ шифрування")
    print("- decrypted.txt - дешифрований текст")
    
    

if __name__ == "__main__":
    main()