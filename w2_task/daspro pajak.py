def hitung_tagihan(minut_kerja, minut_malam, minut_akhir_pekan):
    """
    Menghitung tagihan bulanan dan biaya rata-rata per menit sebelum pajak.
    """
    tarif_bulanan = 3999  # Tarif tetap dalam sen
    menit_bebas = 600
    biaya_per_menit_tambahan = 40  # Biaya per menit tambahan dalam sen
    pajak_persen = 5.25  # Pajak dalam persen

    # Hitung menit tambahan pada hari kerja
    if minut_kerja > menit_bebas:
        menit_tambahan = minut_kerja - menit_bebas
        biaya_tambahan = menit_tambahan * biaya_per_menit_tambahan
    else:
        biaya_tambahan = 0

    # Hitung tagihan sebelum pajak
    tagihan_sebelum_pajak = tarif_bulanan + biaya_tambahan

    # Hitung pajak
    pajak = tagihan_sebelum_pajak * (pajak_persen / 100)

    # Hitung total tagihan
    total_tagihan = tagihan_sebelum_pajak + pajak

    # Hitung biaya rata-rata per menit sebelum pajak
    total_menit = minut_kerja + minut_malam + minut_akhir_pekan
    if total_menit > 0:
        biaya_rata_rata_per_menit = tagihan_sebelum_pajak / total_menit
    else:
        biaya_rata_rata_per_menit = 0

    # Mengembalikan nilai dalam sen
    return {
        "minut_kerja": minut_kerja,
        "minut_malam": minut_malam,
        "minut_akhir_pekan": minut_akhir_pekan,
        "tagihan_sebelum_pajak": tagihan_sebelum_pajak,
        "biaya_rata_rata_per_menit": biaya_rata_rata_per_menit,
        "pajak": pajak,
        "total_tagihan": total_tagihan
    }

while True:
    # Input dari pengguna
    minut_kerja = int(input("Masukkan jumlah menit pada hari kerja: "))
    minut_malam = int(input("Masukkan jumlah menit malam: "))
    minut_akhir_pekan = int(input("Masukkan jumlah menit akhir pekan: "))

    # Hitung tagihan dan biaya rata-rata
    hasil = hitung_tagihan(minut_kerja, minut_malam, minut_akhir_pekan)

    # Tampilkan hasil
    print("\nTagihan dan Biaya:")
    print(f"Tagihan sebelum pajak: ${hasil['tagihan_sebelum_pajak'] / 100:.2f}")
    print(f"Biaya rata-rata per menit: ${hasil['biaya_rata_rata_per_menit'] / 100:.2f}")
    print(f"Pajak: ${hasil['pajak'] / 100:.2f}")
    print(f"Total tagihan: ${hasil['total_tagihan'] / 100:.2f}")

    # Menanyakan kepada pengguna apakah ingin menghitung lagi
    ulang = input("Apakah Anda ingin menghitung lagi? (y/t): ").strip().lower()
    
    # Menghentikan loop jika input bukan 'y'
    if ulang != 'y':
        break

print("Terima kasih telah menggunakan program ini.")