jumlah_penduduk = int(input("Masukkan jumlah penduduk masyarakat: "))

toilet_per_orang = 1 / 3  # Satu toilet untuk setiap 3 orang
liter_per_siram_lama = 15  # Liters per flush for old toilet
liter_per_siram_baru = 2   # Liters per flush for new toilet
jumlah_siram_per_hari = 14  # Times per day
biaya_pemasangan_per_toilet = 150  # Cost in dollars
kurs = 16000
idr = biaya_pemasangan_per_toilet * kurs
#menghitung jumlah toilet
toilet = jumlah_penduduk * toilet_per_orang

#hitung air keluar toilet lama
air_keluar_lama = toilet * liter_per_siram_lama * jumlah_siram_per_hari

#hitung air keluar baru
air_keluar_baru = toilet * liter_per_siram_baru * jumlah_siram_per_hari

#hitung hemat air
hemat = air_keluar_lama - air_keluar_baru

#total biaya pemasangan
pasang = biaya_pemasangan_per_toilet * toilet
pasang_idr = idr * toilet
print(f"Penghematan air per hari adalah {air_keluar_baru:.2f} liter.")
print(f"Total biaya pemasangan untuk toilet baru adalah ${pasang:.2f}.")
print(f"Total biaya pemasangan untuk toilet baru adalah RP{idr:.2f}.")