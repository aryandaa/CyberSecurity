from itertools import cycle

def vigenere_decrypt(ciphertext, key):
    plaintext = ''
    key_cycle = cycle(key)
    for c in ciphertext:
        if c.isalpha():
            k = next(key_cycle)
            base = ord('A') if c.isupper() else ord('a')
            shift = ord(k.lower()) - ord('a')
            decrypted_char = chr((ord(c) - base - shift) % 26 + base)
            plaintext += decrypted_char
        else:
            plaintext += c
    return plaintext

flag1 = "VWKJAIK{zu_oei_rghyjv_wuhs_pdk_mwca_wuh_zi}"
key = 'RPSQM'

print(vigenere_decrypt(flag1, key))  
