def xor_decrypt(ciphertext: bytes, key: bytes) -> bytes:
    return bytes([c ^ key[i % len(key)] for i, c in enumerate(ciphertext)])

# Load ciphertext
with open("encrypted_message.txt", "rb") as f:
    ciphertext = f.read()

# Key dari hasil sebelumnya
key = b'recode_the_earth'

# Dekripsi
plaintext = xor_decrypt(ciphertext, key)
print(plaintext.decode(errors="ignore"))
