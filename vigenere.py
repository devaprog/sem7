from cryptography.fernet import Fernet

def vigenere_cipher(plaintext, key):
    key = key.encode()
    cipher = Fernet(key)
    encrypted_text = cipher.encrypt(plaintext.encode())
    return encrypted_text.decode()

def vigenere_decipher(ciphertext, key):
    key = key.encode()
    cipher = Fernet(key)
    decrypted_text = cipher.decrypt(ciphertext.encode())
    return decrypted_text.decode()

# Example usage:
key = "SECRETKEY"
plaintext = "HELLO"
ciphertext = vigenere_cipher(plaintext, key)
print("Encrypted:", ciphertext)
decrypted_text = vigenere_decipher(ciphertext, key)
print("Decrypted:", decrypted_text)
