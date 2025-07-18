def multi_hex_encode(text, times):
    result = text.encode()
    for _ in range(times):
        result = result.hex().encode()
    return result.decode()

if __name__ == "__main__":
    plaintext = "mXpCTF{}"
    layers = 10
    encrypted = multi_hex_encode(plaintext, layers)
    print(f"Hasil encode {layers}x:")

def xor_bytes(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

hexa = encrypted.encode()
key = b"superkey"

xored = xor_bytes(hexa, key)
print("XORed:", xored)