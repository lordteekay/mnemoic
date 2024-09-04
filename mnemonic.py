import os
import hashlib

def generate_entropy(entropy_bits):
    entropy_bytes = os.urandom(entropy_bits//8)
    entropy_hex = entropy_bytes.hex()
    return entropy_hex

entropy_generated = generate_entropy(128)
print(f"Entropy:{entropy_generated}")