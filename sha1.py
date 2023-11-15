import hashlib

def calculate_sha1(text):
    return hashlib.sha1(text.encode()).hexdigest()

# Example usage:
text = "Hello, SHA-1!"
digest = calculate_sha1(text)

print(f"Text: {text}")
print(f"SHA-1 Digest: {digest}")
