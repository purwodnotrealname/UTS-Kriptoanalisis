def xor_encrypt(plaintext, key): #plaintext in in binary string format, key integer format
    ciphertext = [] #store ciphertext as list of binary string format
    for i in range(len(plaintext)):
        cipher_char = plaintext[i] ^ key # int and int XOR operation
        ciphertext.append(bin(cipher_char))
    return ciphertext

def xor_decrypt(ciphertext, key): #ciphertext in list of binary string format, key integer format
    decrypted_text = [] #store decrypted characters as integers
    for cipher_char in ciphertext:
        decrypted_char = int(cipher_char, 2) ^ key
        decrypted_text.append(decrypted_char)
    return bytes(decrypted_text).decode('utf-8')