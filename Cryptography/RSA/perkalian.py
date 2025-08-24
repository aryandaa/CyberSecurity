p = 3141592653589793238462643383279502884197169 
q = 3141592653589793238462643383279502884197169 
n = p * q
print(f"n = {n}")
T = (p-1) * (q-1)
print(f"Totien (T) = {T}\n")

import math
e = 65537
if math.gcd(e, T)!= 1:
    print(f"❌ Nilai e = {e} tidak relatif prima dengan {T} Silakan pilih bilangan lain.")
    exit()

modinv = pow(e, -1, T)
d = modinv
print(f"D = {d}\n")

from Crypto.Util.number import long_to_bytes, bytes_to_long

plaintext = "mXpCTF{Wh4t_are_y0u_us3_the_ph1_f0r_this_ctf?}"
print(f"Plaintext = {plaintext}\n")

# Konversi string → integer
plaintext_int = bytes_to_long(plaintext.encode())
print(f"Plaintext (int) = {plaintext_int}\n")

# Ubah kembali ke bytes
plaintext_bytes = long_to_bytes(plaintext_int)

# Pecah per 4 byte
block_size = 4
blocks = [plaintext_bytes[i:i+block_size] for i in range(0, len(plaintext_bytes), block_size)]

# Tampilkan tiap blok
for idx, block in enumerate(blocks, start=1):
    print(f"Block {idx}: {block}  (int: {bytes_to_long(block)})")

# ----------------------------
# Tambahan: enkripsi RSA
# ----------------------------
print("\n--- Mulai enkripsi RSA ---\n")
print(f"Public key: (n, e) dengan e = {e}")

# 1) Enkripsi tiap blok 4-byte
cipher_blocks = []
for idx, block in enumerate(blocks, start=1):
    m = bytes_to_long(block)
    c = pow(m, e, n)
    cipher_blocks.append(c)
    print(f"Cipher Block {idx}: {c}  (hex: {hex(c)})")

# 2) Jika memungkinkan, enkripsi seluruh plaintext sekaligus
if plaintext_int < n:
    c_full = pow(plaintext_int, e, n)
    print(f"\nFull ciphertext (int) = {c_full}")
    print(f"Full ciphertext (hex) = {hex(c_full)}")
else:
    c_full = None
    print("\nPlaintext (int) >= n, tidak dapat enkripsi seluruh pesan sekaligus. Gunakan enkripsi blok.")

# 3) Dekripsi verifikasi
print("\n--- Verifikasi dekripsi ---\n")

# Jika ada ciphertext penuh, coba dekripsi dan bandingkan
if c_full is not None:
    rec_int = pow(c_full, d, n)
    rec_bytes = long_to_bytes(rec_int)
    try:
        rec_text = rec_bytes.decode()
    except:
        rec_text = repr(rec_bytes)
    print("Recovered from full ciphertext:", rec_text)

# Dekripsi per blok dan gabungkan, lalu pangkas ke panjang asli
recovered_blocks = []
for idx, c in enumerate(cipher_blocks, start=1):
    m_rec = pow(c, d, n)
    b_rec = long_to_bytes(m_rec)
    # pastikan tiap blok (kecuali mungkin blok terakhir) kembali ke ukuran 4 bytes dengan padding kiri nol
    if idx < len(blocks):
        b_rec = b_rec.rjust(block_size, b'\x00')
    recovered_blocks.append(b_rec)

recovered = b"".join(recovered_blocks)[:len(plaintext_bytes)]
try:
    print("Recovered from block ciphertext:", recovered.decode())
except:
    print("Recovered bytes (repr):", repr(recovered))
