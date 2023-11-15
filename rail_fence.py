def rail_fence_cipher_encrypt(plaintext, rails):
    return ''.join(plaintext[i] for i in range(len(plaintext)) if i % rails == 0)

def rail_fence_cipher_decrypt(ciphertext, rails):
    positions = [i for i in range(len(ciphertext)) if i % rails == 0]
    return ''.join(ciphertext[positions.index(i)] for i in range(len(ciphertext)))

# Example usage:
plaintext = "HELLO"
rails = 2
encrypted_text = rail_fence_cipher_encrypt(plaintext, rails)
print("Encrypted:", encrypted_text)
decrypted_text = rail_fence_cipher_decrypt(encrypted_text, rails)
print("Decrypted:", decrypted_text)
