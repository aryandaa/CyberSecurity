#ini adalah program untuk memfaktorkan atau mencari nilai p dan q dari bilangan n pada RSA
'''pastikan install library sympy dan pycryptodome terlebih dahulu
pip install sympy pycryptodome
'''
from sympy import factorint
from Crypto.Util.number import long_to_bytes

n = 232256804416119081595327853524971653490626130693048043632788176405830820231
faktor = factorint(n)

p, q = list(faktor.keys())
print(f"p = {p}\nq = {q}")

e = 65537
c = 64177395397163304691577111719659943845372216362980151178719880072798156324

T = (p - 1) * (q - 1)
print (f"nilai Totien = {T}")

d = pow(e, -1, T)
print (f"kunci dekripsi = {d}")

m = pow(c, d, n)
print (f"plainteks = {m}")

plaintext = long_to_bytes(m)
print(f"Plaintext = {plaintext}")
