from cryptography.fernet import Fernet

def columnar_transposition_encrypt(plaintext, key):
    # Pad the plaintext to make it a multiple of the key length
    pad_length = len(key) - len(plaintext) % len(key)
    plaintext += ' ' * pad_length
    
    # Rearrange the characters based on the key
    rearranged_text = ''.join(plaintext[i::len(key)] for i in range(len(key)))

    # Use Fernet symmetric encryption for added security
    key = key.encode()
    cipher = Fernet(key)
    encrypted_text = cipher.encrypt(rearranged_text.encode())
    return encrypted_text.decode()

def columnar_transposition_decrypt(ciphertext, key):
    key = key.encode()
    cipher = Fernet(key)
    decrypted_text = cipher.decrypt(ciphertext.encode())
    
    # Unshuffle the characters based on the key
    key_length = len(key)
    original_length = len(decrypted_text)
    rows = original_length // key_length
    unshuffled_text = ''.join(decrypted_text[i * rows:(i + 1) * rows] for i in range(key_length)).rstrip()
    return unshuffled_text

# Example usage:
key = "KEY"
plaintext = "HELLO"
ciphertext = columnar_transposition_encrypt(plaintext, key)
print("Encrypted:", ciphertext)
decrypted_text = columnar_transposition_decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)
