import random

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
        text = text + ' ' * (self.key - len(text) % self.key)
        encrypted = ''.join(text[i::self.key] for i in range(self.key))
        return encrypted

    def transposition_decrypt(self, text):
        rows = len(text) // self.key
        decrypted = ''.join(text[i::rows] for i in range(rows))
        return decrypted.strip()

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
        decrypted = ''.join(chr((ord(char) * pow(self.key, -1, 256)) % 256) for char in text)
        return decrypted


if __name__ == "__main__":
    key = 5  # Example key
    cipher = Cipher(key)

    text = "Hello, World!"

    # Substitution
    encrypted = cipher.substitution_encrypt(text)
    decrypted = cipher.substitution_decrypt(encrypted)
    print("Substitution:", encrypted, "->", decrypted)

    # Transposition
    encrypted = cipher.transposition_encrypt(text)
    decrypted = cipher.transposition_decrypt(encrypted)
    print("Transposition:", encrypted, "->", decrypted)

    # Gamma
    encrypted = cipher.gamma_encrypt(text)
    decrypted = cipher.gamma_decrypt(encrypted)
    print("Gamma:", encrypted, "->", decrypted)

    # Analytical Transform
    encrypted = cipher.analytical_transform_encrypt(text)
    decrypted = cipher.analytical_transform_decrypt(encrypted)
    print("Analytical Transform:", encrypted, "->", decrypted)