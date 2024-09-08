def ubahKeGmt7(time_str):
    jam, menit, detik = map(int, time_str.split(':'))
    jam += 5  
    if jam >= 24:
        jam -= 24
    return f"{jam:02}:{menit:02}:{detik:02}"

def perbedaanWaktu(waktuEvent, waktuSekarang):
    jamEvent, menitEvent, detikEvent = map(int, waktuEvent.split(':'))
    jamSekarang, menitSekarang, detikSekarang = map(int, waktuSekarang.split(':'))

    totalDetikEvent = jamEvent * 3600 + menitEvent * 60 + detikEvent
    totalDetikSekarang = jamSekarang * 3600 + menitSekarang * 60 + detikSekarang

    if totalDetikEvent <= totalDetikSekarang:
        print("See you on the next Pear Event!")
    else:
        selisihWaktu = totalDetikEvent - totalDetikSekarang
        jam, reminder = divmod(selisihWaktu, 3600)
        menit, detik = divmod(reminder, 60)
        print(f"{jam:02}:{menit:02}:{detik:02}")

print("Masukkan waktu Stream Event pada zona waktu GMT+2 (HH:MM:SS):")
waktuEvent = input().strip()

print("Masukkan waktu saat ini pada zona waktu GMT+7 (HH:MM:SS):")
waktuSekarang = input().strip()

waktuAkhir = ubahKeGmt7(waktuEvent)
perbedaanWaktu(waktuAkhir, waktuSekarang)
waktuAkhir = ubahKeGmt7(waktuEvent)