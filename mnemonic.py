import os
import hashlib

def generate_entropy(entropy_bits):
    entropy_bytes = os.urandom(entropy_bits//8)
    entropy_hex = entropy_bytes.hex()
    return entropy_hex

entropy_generated = generate_entropy(128)
print(f"Entropy:{entropy_generated}")

def add_checksum(entropy_hex):
    entropy_bin = bin(int(entropy_hex,16))[2:].zfill(len(entropy_hex)*4)
    print(entropy_bin)
    print(f"entropy_bin_len:{len(entropy_bin)}")

add_checksum(entropy_generated)