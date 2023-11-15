from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
import hashlib

def aes_crypt(data, key, mode):
    key = hashlib.sha256(key.encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    return b64encode(cipher.encrypt(pad(data.encode(), AES.block_size))) if mode == 'encrypt' else unpad(cipher.decrypt(b64decode(data)), AES.block_size).decode()

# Example usage:
secret_key = input("Enter the secret key: ")
original_string = input("Enter the original string: ")

encrypted_string = aes_crypt(original_string, secret_key, 'encrypt')
decrypted_string = aes_crypt(encrypted_string, secret_key, 'decrypt')

print("\nAES Encryption and Decryption\n----------")
print(f"Original String: {original_string}")
print(f"Encrypted String: {encrypted_string}")
print(f"Decrypted String: {decrypted_string}")
