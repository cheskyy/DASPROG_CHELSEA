while True:
    berat = float(input("Masukkan berat anda (pon):"))
    tinggi = float(input("Masukkan tinggi anda (inh):"))
    imt = (703 * berat)/tinggi**2
    
    pembulatan = round(imt, 1)
    
    if pembulatan < 18.5:
        print("Berat badan kurang")
    elif 18.5 <= pembulatan <= 24.9:
        print("Normal")
    elif 25.0 <= pembulatan <= 29.9:
        print("Kelebihan berat badan")
    elif pembulatan >= 30.0:
        print("Obesitas")

    # Menanyakan kepada pengguna apakah ingin menghitung lagi
    ulang = input("Apakah Anda ingin menghitung lagi? (y/t): ").strip().lower()
    
    # Menghentikan loop jika input bukan 'y'
    if ulang != 'y':
        break

print("Terima kasih telah menggunakan program ini.")