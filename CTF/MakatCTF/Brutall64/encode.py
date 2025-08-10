from base64 import b64encode
from random import randint

flag = b'mXpCTF{...}'
b64ciper = flag

for i in range(randint(1, 30)):
    b64ciper = b64encode(b64ciper)
print(b64ciper)
open('crazy_cipher.txt', 'w').write(b64ciper.decode())