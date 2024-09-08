# Input dari pengguna
nilai_diinginkan = input("Masukkan nilai yang diinginkan (untuk B): ")
rata_rata_minimum_diperlukan = float(input("Masukkan rata-rata minimum yang diperlukan: "))
rata_rata_saat_ini = float(input("Masukkan rata-rata saat ini pada kursus: "))
persentase_ujian_akhir = float(input("Masukkan berapa jumlah akhir yang dihitung sebagai persentase nilai mata kuliah : "))
# Menghitung persentase kontribusi dari nilai saat ini
persentase_nilai_saat_ini = 100 - persentase_ujian_akhir
# Menghitung skor yang dibutuhkan di ujian akhir
skor_dibutuhkan = (rata_rata_minimum_diperlukan - (rata_rata_saat_ini * (persentase_nilai_saat_ini / 100))) / (persentase_ujian_akhir / 100)
# Output
print(f"Anda membutuhkan skor {skor_dibutuhkan:.2f} di final untuk mendapatkan nilai {nilai_diinginkan}.")