def hitung_sisa_mobil(M, N, waktu_hijau, total_mobil):
    if waktu_hijau <= 0 or total_mobil == 0:
        return total_mobil
    else:
        # 1 mobil melewati lampu hijau setiap 5 detik
        return hitung_sisa_mobil(M - 1, N, waktu_hijau - 5, total_mobil - 1)

def traffic_light(M, N, T):
    # Total waktu lampu hijau yang tersedia setelah merah dan kuning
    waktu_hijau = max(0, T - 25)  # 20 detik merah + 5 detik kuning = 25 detik sebelum hijau
    total_mobil = M + N
    
    # Hitung sisa mobil setelah semua mobil yang bisa lewat
    sisa_mobil = hitung_sisa_mobil(M, N, waktu_hijau, total_mobil)
    
    # Jika tidak ada mobil yang tersisa, berarti semua mobil bisa lewat
    if sisa_mobil == 0:
        print("Semua mobil dapat melewati lampu lalu lintas.")
    else:
        print(f"Ada {sisa_mobil} mobil yang masih tertinggal.")
    
    # Tampilkan jumlah mobil yang tersisa
    print(sisa_mobil)

# Contoh penggunaan:
M, N, T = map(int, input("Masukkan M, N, dan T (misal: 5 3 40): ").split())
traffic_light(M, N, T)