from operations_1 import xor_encrypt, xor_decrypt
from operations_2 import caesar_encrypt, caesar_decrypt
from operation_attack import attack_sim

def main():
    print("UTS Kriptoanalisis ")
    print("Select Encryption Mode:")
    print("1. standard xor")
    print("2. Caesar cipher")
    print("3. Attack simulation")
    
    mode_choice = input("\nEnter choice : ")
    
    
    key = "new" # hardcoded key panjang 2 bytes
    key_bytes = key.encode('utf-8') # string to bytes

    key_bits = '1010' # 4 bit key hardcoded 
    pka_bits = '10' # partial key attack bits (sebagian informasi dari key_bits
    cipher_bits = '1000101011110010'

    if mode_choice == '1': # penyelesaian soal no 1
        plaintext_raw = input("Enter 2 char") # Masukkan string plaintext
        plaintext_bytes = plaintext_raw.encode('utf-8') # encode string ke bytes    

        encrypt_result = xor_encrypt(plaintext_bytes, key_bytes)
        ciphertext = encrypt_result
        print(" ".join(ciphertext))

        decrypt_result = xor_decrypt(ciphertext, key_bytes)
        print("Decrypted Text:", decrypt_result)

    elif mode_choice == '2':

        plaintext_raw = input("Enter 2 char") # Masukkan string plaintext
        plaintext_bytes = plaintext_raw.encode('utf-8') # encode string ke bytes

        caesar_encrypt_result = caesar_encrypt(plaintext_raw, 3) # shift 3 kali
        print("Caesar Encrypted Text:", caesar_encrypt_result)

        caesar_decrypt_result = caesar_decrypt(caesar_encrypt_result, 3)
        print("Caesar Decrypted Text:", caesar_decrypt_result)

    elif mode_choice == '3':
        operation_attack_result = attack_sim(cipher_bits, pka_bits)
        print("Attack Simulation Result:", operation_attack_result)
    else:
        print("Invalid mode selection.")
        return

if __name__ == "__main__":
    main()
