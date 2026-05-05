def attack_sim(cipherbits, pkabits):
    """
    Simulasi Partial Key Attack (PKA).
    Mencari kemungkinan kunci penuh berdasarkan sebagian kunci (pka_bits)
    yang diketahui dan mengujinya terhadap ciphertext.
    """
    print("\n" + "="*40)
    print("MAMULAI SIMULASI PARTIAL KEY ATTACK")
    print("="*40)
    print(f"Ciphertext (bits)       : {cipherbits}")
    print(f"Known Partial Key (bits): {pkabits}")
    
    # Asumsi panjang kunci adalah 4 bit (karena key_bits pada main.py adalah '1110')
    target_key_length = 4
    
    # Hitung berapa bit yang harus di brute-force
    missing_bits_len = target_key_length - len(pkabits)
    
    if missing_bits_len < 0:
        return "Panjang pka_bits melebihi target panjang kunci."

    print(f"\n[INFO] Panjang kunci target: {target_key_length} bit.")
    print(f"[INFO] Terdapat {missing_bits_len} bit yang tidak diketahui.")
    print(f"[INFO] Melakukan brute-force untuk {2**missing_bits_len} kemungkinan sisa bit...\n")

    possible_keys = []
    
    # 1. Hasilkan semua kemungkinan kunci berdasarkan awalan pkabits
    for i in range(2 ** missing_bits_len):
        # Format iterasi menjadi biner dengan padding 0 di depan sesuai jumlah bit yang hilang
        missing_bits = f"{i:0{missing_bits_len}b}"
        candidate_key = pkabits + missing_bits
        possible_keys.append(candidate_key)

    # 2. Uji setiap kandidat kunci dengan ciphertext
    results = []
    for key in possible_keys:
        # Buat kunci yang berulang (repeating key) agar panjangnya sama dengan ciphertext
        repeated_key = ""
        while len(repeated_key) < len(cipherbits):
            repeated_key += key
        # Potong jika kelebihan agar pas dengan panjang ciphertext
        repeated_key = repeated_key[:len(cipherbits)]
        
        # Lakukan operasi XOR antara cipherbits dan repeated_key
        plaintext_bits = ""
        for c_bit, k_bit in zip(cipherbits, repeated_key):
            # XOR bit per bit
            xor_result = int(c_bit) ^ int(k_bit)
            plaintext_bits += str(xor_result)
            
        results.append({
            'key': key,
            'plaintext': plaintext_bits
        })
        
        print(f"[+] Mencoba Kunci: {key}")
        print(f"    Repeated Key : {repeated_key}")
        print(f"    Hasil Plain  : {plaintext_bits}\n")

    print("="*40)
    print("KESIMPULAN SERANGAN")
    print("="*40)
    print("Analisis dapat melihat 'Hasil Plain' di atas. Kunci yang benar (key_bits)")
    print("adalah kunci yang menghasilkan plaintext yang masuk akal (misalnya memenuhi")
    print("pola format teks tertentu seperti ASCII yang terbaca).")
    print(f"Jika key_bits asli adalah '1110', maka perhatikan hasil dari kunci '1110'.")
    
    return results