from operations_1 import xor_encrypt, xor_decrypt
from operations_2 import caesar_encrypt, caesar_decrypt

def main():
    print("UTS Kriptoanalisis ")
    print("Select Encryption Mode:")
    print("1. standard xor")
    print("2. Caesar cipher")
    print("3. unassigned command")
    
    mode_choice = input("\nEnter choice : ")
    
    plaintext_raw = input("Enter 2 char") # Masukkan string plaintext
    plaintext_bytes = plaintext_raw.encode('utf-8') # encode string ke bytes
    
    key = "NT" # hardcoded key panjang 2 bytes
    key = int.from_bytes(key.encode('utf-8'), byteorder='big') # string to integer

    if mode_choice == '1': # penyelesaian soal no 1
        encrypt_result = xor_encrypt(plaintext_bytes, key)
        ciphertext = encrypt_result
        print(" ".join(ciphertext))

        decrypt_result = xor_decrypt(ciphertext, key)
        print("Decrypted Text:", decrypt_result)

    elif mode_choice == '2':
        caesar_encrypt_result = caesar_encrypt(plaintext_raw, 3) # 
        print("Caesar Encrypted Text:", caesar_encrypt_result)

        caesar_decrypt_result = caesar_decrypt(caesar_encrypt_result, 3)
        print("Caesar Decrypted Text:", caesar_decrypt_result)


    elif mode_choice == '3':
        print("unassigned command")
    else:
        print("Invalid mode selection.")
        return

if __name__ == "__main__":
    main()
