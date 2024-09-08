# Input dari pengguna
kecepatan = int(input("Masukkan kecepatan lepas landas (km/jam): "))
jarak_meter = int(input("Masukkan jarak ketapel (meter): "))

# Konversi kecepatan dari km/jam ke m/s
kecepatan_ms = kecepatan * 1000 / 3600

# Menghitung percepatan (a = v^2 / (2 * s))
percepatan = (kecepatan_ms ** 2) / (2 * jarak_meter)

# Menghitung waktu (t = v / a)
waktu = kecepatan_ms / percepatan

# Output
print(f"Percepatan = {percepatan:.2f} m/s².")
print(f"Waktu yang dibutuhkan kecepatan lepas landas = {waktu:.2f} detik.")

#^