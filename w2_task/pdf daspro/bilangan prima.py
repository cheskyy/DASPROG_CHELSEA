def adalah_prima(n):
    if n <= 2:
        return False  # Bilangan kurang dari atau sama dengan 1 bukan bilangan prima
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Jika n habis dibagi i, maka n bukan bilangan prima
    return True  # Jika tidak ada pembagi selain 1 dan n, maka n adalah bilangan prima

# Meminta input dari pengguna
bilangan = int(input("Masukkan sebuah bilangan: "))

# Mengecek apakah bilangan tersebut prima atau tidak
if adalah_prima(bilangan):
    print(f"{bilangan} adalah bilangan prima.")
else:
    print(f"{bilangan} bukan bilangan prima.")
