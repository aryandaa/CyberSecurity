UP = ord('A')
LOW = ord('a')

def Encryption(pt, key):
    ct = ''
    
    for i, p in enumerate(pt):
        if p.isupper():
            ct += chr(((ord(p) - UP) - (ord(key[i % len(key)].upper()) - UP)) % 26 + UP)
        elif p.islower():
            ct += chr(((ord(p) - LOW) - (ord(key[i % len(key)].lower()) - LOW)) % 26 + LOW)
        else:
            ct += p
    return ct

flag = 'yXcVNQ{h193h3j3_1mo_f3xg_f3n3laru_k4nq1_n43s4k}'
key = 'MANTULS'

print(Encryption(flag, key))