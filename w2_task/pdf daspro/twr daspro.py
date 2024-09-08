print("-------------------------------------------------------------")
print("                   Program The Witch's Riddle                ")
print("-------------------------------------------------------------\n")

# Meminta input 7 angka satu per satu
print("Masukkan 7 angka (pisahkan dengan spasi): ")
a1, a2, a3, a4, a5, a6, a7 = input().split()  # Membaca input sebagai string
a1, a2, a3, a4, a5, a6, a7 = int(a1), int(a2), int(a3), int(a4), int(a5), int(a6), int(a7)

# Meminta input untuk jumlah kucing yang akan melompat dan berapa kali lompat
b = int(input("Masukkan jumlah kucing yang melompat ke depan: "))
c = int(input("Masukkan berapa kali lompatan: "))

# Meminta input untuk tiga indeks yang dibutuhkan
d = int(input("Masukkan indeks pertama (antara 0 hingga 6): "))
e = int(input("Masukkan indeks kedua (antara 0 hingga 6): "))
f = int(input("Masukkan indeks ketiga (antara 0 hingga 6): "))

# Memasukkan semua angka ke dalam variabel array
a = [a1, a2, a3, a4, a5, a6, a7]

# Melakukan lompatan sebanyak c kali
for i in range(c):
    temp = [0] * 7
    for j in range(7):
        temp[(j + b) % 7] = a[j]  # Rotasi yang benar, memindahkan elemen ke depan
    a = temp  # Perbarui array

# Menampilkan hasil
print("\n-------------------------------------------------------------")
print(f"Hasil angka pada indeks {d}, {e}, dan {f} adalah = {a[d]} {a[e]} {a[f]}")
print("-------------------------------------------------------------")
