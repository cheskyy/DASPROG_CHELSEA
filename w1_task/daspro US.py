print("mari melihat cara tukar mata uang!")
# Konstanta nilai tukar
nilai_kurs = 0.65  # 1 USD = 0.65 GBP

# Input dari pengguna: jumlah uang dalam dolar AS
usd = float(input("Masukkan jumlah uang dalam dolar AS (USD): "))

# Menghitung jumlah uang dalam poundsterling Inggris
gbp = usd * nilai_kurs

# Output: jumlah uang dalam poundsterling Inggris
print(f"{usd} USD setara dengan {gbp:.2f} GBP.")