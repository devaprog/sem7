import numpy as np

def hill_cipher_encrypt(plaintext, key_matrix):
    plaintext = [ord(char) - ord('A') for char in plaintext.upper() if 'A' <= char <= 'Z']
    padded_length = len(key_matrix)
    plaintext += [0] * (padded_length - len(plaintext) % padded_length)  # Pad if necessary
    plaintext_matrix = np.array(plaintext).reshape(-1, padded_length)

    encrypted_matrix = np.dot(plaintext_matrix, key_matrix) % 26
    encrypted_text = ''.join([chr(char + ord('A')) for row in encrypted_matrix for char in row])
    return encrypted_text

def hill_cipher_decrypt(ciphertext, key_matrix):
    ciphertext = [ord(char) - ord('A') for char in ciphertext.upper() if 'A' <= char <= 'Z']
    ciphertext_matrix = np.array(ciphertext).reshape(-1, len(key_matrix))

    inverse_key_matrix = np.linalg.inv(key_matrix)
    decrypted_matrix = np.dot(ciphertext_matrix, inverse_key_matrix).round() % 26
    decrypted_text = ''.join([chr(int(char) + ord('A')) for row in decrypted_matrix for char in row])
    return decrypted_text

# Example usage:
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
plaintext = "HELLO"
ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
print("Encrypted:", ciphertext)
decrypted_text = hill_cipher_decrypt(ciphertext, key_matrix)
print("Decrypted:", decrypted_text)
