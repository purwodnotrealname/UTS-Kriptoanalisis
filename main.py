from encrypt import xor_encrypt

def main():
    print("--- Binary Encryption Utility ---")
    print("Select Encryption Mode:")
    print("1. standard xor")
    print("2. unassigned command")
    print("3. unassigned command")
    
    mode_choice = input("\nEnter choice : ")
    
    plaintext_raw = input("Enter 2 char") #enter raw char plaintext
    plaintext_bin = ''.join(format(ord(char), '08b') for char in plaintext_raw) #char to binary
    
    key = 0b00111001
    #key = 0b0011010110011101 16 bit key

    if mode_choice == '1':
        raw_result = xor_encrypt(plaintext_bin, key)
        ciphertext = [bin(ord(c)) for c in raw_result]

    elif mode_choice == '2':
        print("unassigned command")
    elif mode_choice == '3':
        print("unassigned command")
    else:
        print("Invalid mode selection.")
        return

    print("\nResulting Binary Ciphertext:")
    print(" ".join(ciphertext))

if __name__ == "__main__":
    main()
