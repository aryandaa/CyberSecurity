def decrypt_variable_caesar(ciphertext):
    shifts = [1,2,3,4,5,1,2,3,4,5]  # Daftar pergeseran
    decrypted = ""
    idx = 0

    for char in ciphertext:
        if char.isalpha():
            shift = shifts[idx % len(shifts)]
            if char.islower():
                decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif char.isupper():
                decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            idx += 1
        else:
            decrypted += char
    return decrypted

cipher = """
Uq qd gwiwoco qpxh,  
Lj zqx mpng yikv rfuvelf lr zqxv icqhx, 
wljo L mbxh ifhlii prx ppoc gcwi, dxx ukpi jvviqg. JNUWNWB{ary_bnpsxu_wljsg}  
Gdgm nhxyft M tgqh uq ctv pewdjhw xkwl b seyugur bno nuu sbo, 
e sjbxmn vlfqgg gz wmrf lxxfni.  
Bsz cui ujh hsqzr ph qd gptnsg, fof M zkhpi ob xpwo yp bsz. 
Oiy VUYXU jyneg ctv wlwpwjl ujh kjpdp dksljs. JNUWNWB{vki_lgb_nt_WVZTV}
"""
print(decrypt_variable_caesar(cipher)) 
print(cipher)