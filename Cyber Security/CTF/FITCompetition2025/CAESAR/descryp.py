def caesar_decrypt(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            decrypted += char
    return decrypted

def main():
    file_path = "love.txt"
    shift = 3  # Default Caesar shift

    with open(file_path, 'r', encoding='utf-8') as f:
        encrypted_text = f.read()

    decrypted_text = caesar_decrypt(encrypted_text, shift)

    print("Decrypted Content:\n")
    print(decrypted_text)

if __name__ == "__main__":
    main()
