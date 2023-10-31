import hashlib

def sha256_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

# Example usage:
data = "Hello, World!"
hashed = sha256_hash(data)
print("SHA-256 Hash:", hashed)
