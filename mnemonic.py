import os
import hashlib

def generate_entropy(entropy_bits):
    entropy_bytes = os.urandom(entropy_bits//8)
    entropy_hex = entropy_bytes.hex()
    return entropy_hex

entropy_generated = generate_entropy(128)

def add_checksum(entropy_hex):
    entropy_bin = bin(int(entropy_hex,16))[2:].zfill(len(entropy_hex)*4)
    sha_hash = bin(int(hashlib.sha256(bytes.fromhex(entropy_hex)).hexdigest(),16))[2:].zfill(256)
    checksum_len = len(entropy_bin)//32
    checksum = sha_hash[:checksum_len]
    checksum_with_entropy = entropy_bin + checksum
    return checksum_with_entropy

add_checksum(entropy_generated)
def get_wordlist():
    with open('cleaned_wordlist.txt','r') as file:
        wordlist = file.read().splitlines()
        print(f"worldlist_len:{len(wordlist)}")

get_wordlist()
