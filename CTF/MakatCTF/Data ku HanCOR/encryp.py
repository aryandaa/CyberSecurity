# cara yanda membuat enkripsinya
def encrypt(flag, key):
    enc = ''
    for i in range(len(flag)):
        print(flag[i])
        print(int(ord(flag[i])))
        enc += chr(int(ord(flag[i])) ^ int(ord(key[i % len(key)])))
    return enc

flag = open('./Data ku HanCOR/data.txt', 'r').read().strip()
print(flag)
key = 'secret'

open('data.txt', 'w').write(encrypt(flag, key))