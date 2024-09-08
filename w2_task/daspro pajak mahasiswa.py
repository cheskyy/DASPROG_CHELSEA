while True:
    # Meminta input harga dari pengguna
    harga = int(input("Masukkan total harga: "))
    
    # Menampilkan pilihan
    print("Jenis pilihan :")
    print("\t1. Non-Mahasiswa")
    print("\t2. Mahasiswa")
    
    # Meminta input pilihan dari pengguna
    pilihan = int(input("Masukkan Pilihan Anda: "))

    # Persentase diskon dan PPN
    diskon = 20 / 100
    ppn = 5 / 100

    # Menghitung harga berdasarkan pilihan
    if pilihan == 1:
        harga_ppn = harga * ppn
        harga_total = harga + harga_ppn
        print(f"Maka total Harga Anda: Rp.{harga_total:.2f}")
    elif pilihan == 2:
        besar_diskon = harga * diskon
        harga_ppn = harga * ppn
        harga_diskon = harga - besar_diskon
        harga_total = harga_diskon + harga_ppn
        print(f"Maka total Harga Anda: Rp.{harga_total:.2f}")
    else:
        print("there is no other choice!")

    # Menanyakan kepada pengguna apakah ingin menghitung lagi
    ulang = input("Apakah Anda ingin menghitung lagi? (y/t): ").strip().lower()
    
    # Menghentikan loop jika input bukan 'y'
    if ulang != 'y':
        break

print("Terima kasih telah menggunakan program ini.")