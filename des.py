from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding as asy_padding
from cryptography.hazmat.primitives import hashes

class DES:
    def __init__(self):
        try:
            self.inputmessage = input("Enter message to encrypt: ")
            self.key = self.generate_symmetric_key()
            self.encrypted_data = self.encrypt(self.key, self.inputmessage)
            print("Encrypted message:", self.encrypted_data.decode())
            decrypted_message = self.decrypt(self.key, self.encrypted_data)
            print("Decrypted message:", decrypted_message.decode())
        except Exception as e:
            print(e)

    def generate_symmetric_key(self):
        key = b"mysecretpassword"  # Replace with a strong key generation mechanism
        return key

    def encrypt(self, key, plaintext):
        cipher = Cipher(algorithms.TripleDES(key), modes.ECB())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(64).padder()
        padded_data = padder.update(plaintext.encode()) + padder.finalize()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        return encrypted_data

    def decrypt(self, key, ciphertext):
        cipher = Cipher(algorithms.TripleDES(key), modes.ECB())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = padding.PKCS7(64).unpadder()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
        return unpadded_data


if __name__ == "__main__":
    des = DES()
