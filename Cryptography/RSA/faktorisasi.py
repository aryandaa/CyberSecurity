#ini adalah program untuk memfaktorkan atau mencari nilai p dan q dari bilangan n pada RSA
'''pastikan install library sympy dan pycryptodome terlebih dahulu
pip install sympy pycryptodome
'''
from sympy import factorint
from Crypto.Util.number import long_to_bytes

n = 5494889822185956411984423766256223313786685815183189826675961721333333848402827335961450708336521929684310067360490956009008787423860222518129639986685553

faktor = factorint(n)

p, q = list(faktor.keys())
print(f"p = {p}\nq = {q}")

e =  65537
c = 2437835326876557482809902984416342913092929865141814181325822805060877949493396832059983533813374300648874266950296012487467889652861472676426012847392193

T = (p - 1) * (q - 1)
print (f"nilai Totien = {T}")

d = pow(e, -1, T)
print (f"kunci dekripsi = {d}")

m = pow(c, d, n)
print (f"plainteks = {m}")

plaintext = long_to_bytes(m)
print(f"Plaintext = {plaintext}")
