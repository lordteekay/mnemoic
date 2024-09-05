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
    checksum = sha_hash[:136]
    checksum_with_entropy = entropy_bin + checksum
    return checksum_with_entropy

checksum_with_entropy=add_checksum(entropy_generated)
def get_wordlist():
    with open('cleaned_wordlist.txt','r') as file:
        wordlist = file.read().splitlines()
        return wordlist

def binary_mnemonic_word(checksum):
    wordlist = get_wordlist()
    mnemonic = []
    print(f"checksum_len:{len(checksum)}")
    for i in range (0, len(checksum), 11):
        index = int(checksum[i:i+11],2)
        mnemonic.append(wordlist[index])
    return " ".join(mnemonic)


mnemonic = binary_mnemonic_word(checksum_with_entropy)
print(f"mnemoic:{mnemonic}")