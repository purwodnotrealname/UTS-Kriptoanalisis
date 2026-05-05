# reference https://www.geeksforgeeks.org/ethical-hacking/caesar-cipher-in-cryptography/
def caesar_encrypt(plaintext, shift): # plaintext_raw string dan shift integer
    ciphertext = "" # storing
    for char in plaintext:
        if char.isalpha(): # char.isalpha() checking alphabetic character
            shift_amount = shift % 26 # mod 26
            if char.islower(): # cek kapitalitasi karakter
                base = ord('a') 
            else:
                base = ord('A')
            encrypted_char = chr((ord(char) - base + shift_amount) % 26 + base) # shift karakter
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            decrypted_char = chr((ord(char) - base - shift_amount) % 26 + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text