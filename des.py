from Crypto.Random import get_random_bytes

class DES:
    def __init__(self):
        try:
            message = input("Enter message to encrypt: ")
            key = get_random_bytes(8)  # 8 bytes for DES
            encrypted_data = self.crypt(message, key, 'encrypt')
            print("Encrypted message:", encrypted_data.decode())
            decrypted_message = self.crypt(encrypted_data, key, 'decrypt')
            print("Decrypted message:", decrypted_message.decode())
            print("DES Symmetric Key:", key.hex())
        except Exception as e:
            print(e)

    def crypt(self, data, key, mode):
        cipher = DES3.new(key, DES3.MODE_ECB)
        if mode == 'encrypt':
            return b64encode(cipher.encrypt(pad(data.encode(), DES3.block_size)))
        elif mode == 'decrypt':
            return unpad(cipher.decrypt(b64decode(data)), DES3.block_size).decode()

if __name__ == "__main__":
    des = DES()
