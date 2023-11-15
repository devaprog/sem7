from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

def diffie_hellman_key_exchange():
    # Generate private key and public key
    private_key = dh.generate_parameters(generator=2, key_size=2048)
    public_key = private_key.generate_private_key()

    # Serialize and exchange public keys
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Deserialize received public key
    received_public_key = serialization.load_pem_public_key(public_key_bytes)

    # Derive shared key
    shared_key = public_key.exchange(received_public_key)

    return shared_key

# Example usage:
alice_shared_key = diffie_hellman_key_exchange()
bob_shared_key = diffie_hellman_key_exchange()

print("Alice's Shared Key:", alice_shared_key.hex())
print("Bob's Shared Key:", bob_shared_key.hex())
