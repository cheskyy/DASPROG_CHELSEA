bilangan = int(input("Masukkan bilangan bulat:"))  # Input bilangan bulat
bil_str = str(bilangan) #Mengubah int menjadi string

if '4' in bil_str:
        print("SEVER")
else:
       print("UNITE")
while True:
    bilangan = int(input("Masukkan bilangan bulat (-100000 hingga 100000), atau ketik 'q' untuk keluar: "))
    
    if bilangan == 'q':
        print("Program dihentikan.")
        break
    
    if -100000 <= bilangan <= 100000:  # Memberi batasan sesuai soal
        bil_str = str(bilangan)  # Mengubah int menjadi string
        if '4' in bil_str:  # Percabangan menentukan bilangan mengandung angka 4 atau tidak
            print("SEVER")
        else:
            print("UNITE")
    else:
        print("Diluar jangkauan")

    lanjut = input("Apakah ingin memasukkan bilangan lagi? (y/n): ")
    if lanjut.lower() != 'y':
        break