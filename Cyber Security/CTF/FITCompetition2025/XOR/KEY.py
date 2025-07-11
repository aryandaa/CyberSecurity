with open('key.hex', 'r') as f:
    key = bytes.fromhex(f.read().strip())
print("Key:", key)