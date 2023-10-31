def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Example usage:
text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Encrypted:", encrypted_text)
decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted:", decrypted_text)
