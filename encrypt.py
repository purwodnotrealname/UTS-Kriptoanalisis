def xor_encrypt(plaintext, key):
    ciphertext = []
    for i in range(len(plaintext)):
        cipher_char = plaintext[i] ^ key
        ciphertext.append(bin(cipher_char))
    return ciphertext

def xor_decrypt(ciphertext, key):
