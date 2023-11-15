from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend

def generate_dsa_keypair():
    private_key = dsa.generate_private_key(key_size=2048, backend=default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key, message):
    signature = private_key.sign(message.encode(), hashes.SHA256())
    return signature

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(signature, message.encode(), hashes.SHA256())
        return True
    except dsa.InvalidSignature:
        return False

# Example usage:
private_key, public_key = generate_dsa_keypair()
message = "Hello, DSS!"
signature = sign_message(private_key, message)

print(f"Message: {message}")
print(f"Signature: {signature.hex()}")
print(f"Signature Verified: {verify_signature(public_key, message, signature)}")
