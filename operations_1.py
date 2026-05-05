def xor_encrypt(plaintext, key_bytes): 
    ciphertext = [] #store ciphertext as list of binary string format
    for i in range(len(plaintext)):
        key_byte = key_bytes[i % len(key_bytes)] 
        cipher_char = plaintext[i] ^ key_byte
        ciphertext.append(format(cipher_char, '#010b')) 
    return ciphertext


def xor_decrypt(ciphertext, key_bytes): #ciphertext in list of binary string format, key_bytes bytes format
    decrypted_text = [] #store decrypted characters as integers
    for i, cipher_char in enumerate(ciphertext):
        key_byte = key_bytes[i % len(key_bytes)] 
        decrypted_char = int(cipher_char, 2) ^ key_byte
        decrypted_text.append(decrypted_char)
    return bytes(decrypted_text).decode('utf-8')