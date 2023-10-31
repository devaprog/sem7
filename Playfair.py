from Crypto.Cipher import Playfair

def playfair_cipher(plaintext, key):
    cipher = Playfair.new(key.encode())
    encrypted_text = cipher.encrypt(plaintext.encode())
    return encrypted_text.decode()

def playfair_decipher(ciphertext, key):
    cipher = Playfair.new(key.encode())
    decrypted_text = cipher.decrypt(ciphertext.encode())
    return decrypted_text.decode()

# Example usage:
key = "KEYWORD"
plaintext = "HELLO"
ciphertext = playfair_cipher(plaintext, key)
print("Encrypted:", ciphertext)
decrypted_text = playfair_decipher(ciphertext, key)
print("Decrypted:", decrypted_text)
