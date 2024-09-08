def tahun_kabisat(tahun):
    """Mengembalikan 1 jika tahun kabisat, 0 jika tidak."""
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return 1
    return 0

def nomor_hari(d, m, t):
    """Menghitung nomor hari dalam setahun untuk tanggal yang diberikan."""
    # Jumlah hari dalam setiap bulan
    hari_dalam_bulan = [31, 28 + tahun_kabisat(t), 31, 30, 31, 30, 
                        31, 31, 30, 31, 30, 31]

    # Menjumlahkan hari hingga bulan sebelumnya
    nomor_hari = sum(hari_dalam_bulan[:m - 1]) + d
    return nomor_hari

while True:
    # Input dari pengguna
    hari = int(input("Masukkan hari: "))
    bulan = int(input("Masukkan bulan: "))
    tahun = int(input("Masukkan tahun: "))

    # Menghitung dan menampilkan nomor hari
    hasil = nomor_hari(hari, bulan, tahun)
    print(f"Tanggal {hari}/{bulan}/{tahun} adalah hari ke-{hasil} dalam setahun.")

    # Menanyakan kepada pengguna apakah ingin menghitung lagi
    ulang = input("Apakah kamu ingin menghitung lagi? (y/t): ").strip().lower()
    
    # Menghentikan loop jika input bukan 'y'
    if ulang != 'y':
        break

print("Terima kasih telah menggunakan program ini.")