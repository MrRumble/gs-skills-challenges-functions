def encode(text, key):
    cipher = make_cipher(key)
    print(f'encode cipher is: {cipher}')
    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)
    print(f'decoded cipher is: {cipher}')
    plaintext_chars = []
    print(f'encrypted message is {encrypted}')
    for char in encrypted:
        plain_char = cipher[ord(char) - 65]   #char = s we want cipher[4]
        print(65 - ord(char))
        plaintext_chars.append(plain_char)
    print(f'plaintext_chars is {plaintext_chars}')

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 96) for i in range(1, 27)]
    
    print(f"we start by generating a list of letters\n {alphabet}")
    
    cipher_with_duplicates = list(key) + alphabet
    print('we then create a new list called cipher_with_duplicates.')
    print('This changes the string key into a list and adds the alphabet to it.')
    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")



