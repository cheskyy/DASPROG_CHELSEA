# Fungsi untuk menghitung kemiringan garis
def hitung_miring(x1, y1, x2, y2):
    if x2 == x1 and y2 == y1:
        print ("Kemiringan tidak terdefinisi untuk garis vertikal.")
    else:
        return (y2 - y1) / (x2 - x1)

# Fungsi untuk menghitung titik tengah
def hitung_tengah(x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)

# Input dari pengguna
x1 = float(input("Masukkan x koordinat titik pertama: "))
y1 = float(input("Masukkan y koordinat titik pertama: "))
x2 = float(input("Masukkan x koordinat titik kedua: "))
y2 = float(input("Masukkan y koordinat titik kedua: "))

try:
    # Menghitung kemiringan garis antara dua titik
    miring_garis = hitung_miring(x1, y1, x2, y2)

    # Menghitung kemiringan garis tegak lurus (negatif kebalikan dari kemiringan garis)
    miring_tegak_lurus = -1 / miring_garis

    # Menghitung titik tengah
    x_tengah, y_tengah = hitung_tengah(x1, y1, x2, y2)

    # Menghitung intersep (g) dari garis tegak lurus
    g_tegak_lurus = y_tengah - miring_tegak_lurus * x_tengah

    # Menampilkan hasil
    print(f"Persamaan garis tegak lurus dalam bentuk y = mx + g adalah:")
    print(f"y = {miring_tegak_lurus:.2f}x + {g_tegak_lurus:.2f}")

except ValueError as e:
    print(e)