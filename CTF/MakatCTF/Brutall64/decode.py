from base64 import b64decode

with open('crazy_cipher.txt', 'r') as file:
    data = file.read().strip()
decoded = data.encode()

for _ in range(20):
    decoded = b64decode(decoded)

print(decoded.decode())

