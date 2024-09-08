def main():
    # Menampilkan informasi awal
    print("-------------------------------------------------------------")
    print("                   Program Last Man Standing 2              ")
    print("-------------------------------------------------------------")
    print()

    # Meminta input dari pengguna
    N = int(input("Masukkan jumlah bola (N): "))
    C = int(input("Siapa yang mulai? (1 untuk Lala, 2 untuk Lili): "))

    # Selama masih ada bola
    while N > 0:
        # Pemain mengambil bola sebanyak mungkin (5, 2, atau 1)
        if N >= 5:
            N = N - 5
        elif N >= 2:
            N = N - 2
        else:
            N = N - 1

        # Ganti giliran pemain setelah mengambil bola
        if C == 1:
            C = 2  # Jika giliran Lala, ganti ke Lili
        else:
            C = 1  # Jika giliran Lili, ganti ke Lala

    # Ketika bola habis, pemain yang gilirannya terakhir akan kalah
    if C == 1:
        print()
        print("Jawaban Pemenang: Lili")  # Jika giliran terakhir adalah Lala, Lili menang
    else:
        print()
        print("Jawaban Pemenang: Lala")  # Jika giliran terakhir adalah Lili, Lala menang

if __name__ == "__main__":
    main()
