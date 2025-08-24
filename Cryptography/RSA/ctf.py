# RSA super mini + A1Z26

# Step 1: Kunci
p = 3
q = 31415926535897932384626433832795028841
n = p * q  # modulus
phi = (p - 1) * (q - 1)
e = 65537 # kecil biar gampang, asal gcd(e, phi) = 1

# Cari d (mod inverse)
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

d = modinv(e, phi)

# Step 2: Konversi A1Z26
def text_to_a1z26(text):
    return [ord(c.upper()) - 64 for c in text if c.isalpha()]

def a1z26_to_text(nums):
    return ''.join(chr(n + 64) for n in nums)

plaintext = "mXpCTF{Wh4t_are_y0u_us3_the_ph1_f0r_this_ctf?}"
nums = text_to_a1z26(plaintext)

# Step 3: Enkripsi
cipher = [(m ** e) % n for m in nums]

# Step 4: Dekripsi
decrypted_nums = [(c ** d) % n for c in cipher]
decrypted_text = a1z26_to_text(decrypted_nums)

print("n =", n)
print("phi =", phi)
print("e =", e)
print("d =", d)
print("Plaintext A1Z26:", nums)
print("Cipher:", cipher)
print("Decrypted A1Z26:", decrypted_nums)
print("Decrypted Text:", decrypted_text)
