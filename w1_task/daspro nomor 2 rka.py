print("ayooo belajar!")
g = 9.80  # Konstanta gravitasi dalam m/detik^2
efficiency = 0.90  # Efisiensi konversi energi menjadi listrik, yaitu 90%
#Input dari pengguna
tinggi_bendungan = float(input("Masukkan tinggi bendungan (dalam meter): "))
aliran_air = float(input("Masukkan aliran air (dalam meter kubik per detik): "))
#Massa air (1 meter kubik air memiliki massa 1000 kg)
massa_air = aliran_air * 1000  # Massa air dalam kg

#Energi potensial yang dihasilkan (w = m * g * h)
energi_potensial = massa_air * g * tinggi_bendungan  # dalam joule
#Energi listrik yang dihasilkan dengan efisiensi 90%
energi_listrik = energi_potensial * efficiency  # dalam joule
#Mengonversi energi listrik menjadi megawatt (1 watt = 1 joule/detik)
#1 megawatt = 10^6 watt
daya_megawatt = energi_listrik / 10**6  # dalam megawatt
#Output
print(f"Daya yang dihasilkan oleh bendungan adalah sekitar {daya_megawatt:.2f} megawatt.")
