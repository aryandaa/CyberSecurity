def akar_primitif(n):
    """Menemukan akar primitif modulo n."""
    if n <= 2:
        return -1  # Tidak ada akar primitif
    for r in range(2, n):
        # Cek apakah r relatif prima dengan n
        if math.gcd(r, n) == 1:
            # Cek apakah r adalah akar primitif
            is_primitive = True
            for i in range(1, n):
                if pow(r, i, n) == 1:
                    is_primitive = False
                    break
            if is_primitive:
                return r
    return -1  # Tidak ada akar primitif

import math

# Contoh penggunaan:
n = 11 # Masukan modulo yang ingin dicari akar primitifnya
akar = akar_primitif(n)
if akar != -1:
    print(f"Akar primitif modulo {n} adalah: {akar}")
else:
    print(f"Tidak ada akar primitif modulo {n}")