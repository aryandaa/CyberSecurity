#memasukan nilai p dan q
p = 61
q = 53

#menghitung nilai n
n = p * q
print (f"{n}\n")

#menghitung nilai totien
T = (p-1) * (q-1)

#Memilih nilai e
import math
e = 17
if math.gcd(e, T)!= 1:
    print(f"❌ Nilai e = {e} tidak relatif prima dengan {T} Silakan pilih bilangan lain.")
    exit()
    
#Hitung nilai d
modinv = pow(e, -1, T)
d = modinv
# print(f"Nilai d (private key) adalah: {d}\n") 

# Format A=1 sampai Z=26
def text_to_number(text):
    result = []
    for char in text.upper():
        if char == ' ':
            result.append(00)
        elif char.isalpha():
            result.append(ord(char) - 64)
    return result

def number_to_text(numbers):
    return ''.join([' ' if num == 00 else chr(num + 64) for num in numbers])

# ubah angka jadi blok 4 digit (gabungan 2 angka 2-digit)
def create_blocks(nums):
    nums2digit = [f"{n:02}" for n in nums]
    blocks = []

    for i in range(0, len(nums2digit), 2):
        if i + 1 < len(nums2digit):
            block = int(nums2digit[i] + nums2digit[i + 1])
        else:
            block = int(nums2digit[i] + "00")
        blocks.append(block)
    
    return blocks

# Menginputkan plainteks
M = "hellow world"
print (f"teks awal adalah : {M}\n")

# Mengubah plainteks ke angka (1-26)
plaintext_nums = text_to_number(M)
# print(f"Plaintext (angka): {plaintext_nums}\n")

# Membuat blok 4 digit
plaintext_blocks = create_blocks(plaintext_nums)
print(f"Blok 4 digit: {plaintext_blocks}\n")

# Proses enkripsi RSA per blok
c = [pow(m, e, n) for m in plaintext_blocks]
print(f"Angka setelah dienkripsi : {c}\n")

#Proses dekripi RSA
decrypted = [pow(c, d, n) for c in c]
print (f"teks yang sudah di dekripsi {decrypted}\n")

#memisahkan plainteks yang tadi nya 4 digit menjadi 1 huruf saja
def split_teks(blocks):
    digits = []
    for block in blocks:
        block_str = f"{block:04}"  # jaga-jaga biar tetap 4 digit (misalnya 0905)
        digits.append(int(block_str[:2]))
        digits.append(int(block_str[2:]))
    return digits

#memanggil blok yang sudah terpisah
decrypt_4 = split_teks(decrypted)
# print (f"Blok yang sudah di pisah : {decrypt_4}\n")

#mengubah number menjadi teks 
plaintext = number_to_text(decrypt_4)
print (plaintext)   

