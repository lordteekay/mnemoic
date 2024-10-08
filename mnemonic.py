import os
import hashlib
import binascii
import secrets
import ecdsa
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

checksum_with_entropy=add_checksum(entropy_generated)
def get_wordlist():
    with open('cleaned_wordlist.txt','r') as file:
        wordlist = file.read().splitlines()
        return wordlist

def binary_mnemonic_word(checksumEntropy):
    wordlist = get_wordlist()
    mnemonic = []
    print(f"checksum_len:{len(checksumEntropy)}")
    for i in range (0, len(checksumEntropy), 11):
        index = int(checksumEntropy[i:i+11],2)
        mnemonic.append(wordlist[index])
    return " ".join(mnemonic)

mnemonic = binary_mnemonic_word(checksum_with_entropy)
print(f"mnemoic:{mnemonic}")

def seed_generated(mnemoic_phrase):
    salt = "Random_"+secrets.token_hex(16)
    seed = hashlib.pbkdf2_hmac('sha512',mnemoic_phrase.encode(),salt.encode(),2048)
    return binascii.hexlify(seed).decode()

private_key = seed_generated(mnemonic)
print(f"The private_key:{private_key}")
print(f"private_key_len:{len(private_key)}")

def ecdsa_private_key(key):
    new_key = key[:64]
    new_private_key = ecdsa.SigningKey.from_string(binascii.unhexlify(new_key),curve=ecdsa.SECP256k1)
    return binascii.hexlify(new_private_key.to_string()).decode()
Elliptic_private_key = ecdsa_private_key(private_key)
print(f"Elliptic_private_key:{Elliptic_private_key}")
print(f"Lenght:{len(Elliptic_private_key)}")