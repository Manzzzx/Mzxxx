from datetime import datetime

# Fungsi untuk menghitung umur dengan mengambil tanggal lahir sebagai parameter
def hitung_umur(tanggal_lahir):
    # Mendapatkan tanggal hari ini
    tanggal_hari_ini = datetime.now()
    # Menghitung selisih tanggal antara tanggal hari ini dan tanggal lahir
    selisih_tanggal = tanggal_hari_ini - tanggal_lahir

    # Menghitung umur tahun, bulan, dan hari
    tahun = selisih_tanggal.days // 365  # dibagi dengan 365 hari untuk mengetahui jumlah tahun
    sisa_hari = selisih_tanggal.days % 365  # sisa hari setelah dibagi
    bulan = sisa_hari // 30  # dibagi dengan 30 hari untuk mengetahui jumlah bulan
    sisa_hari %= 30  # sisa hari setelah dibagi
    hari = sisa_hari  # hari yang tersisa

    # Menghitung total bulan dan total hari
    total_bulan = tahun * 12 + bulan
    total_hari = selisih_tanggal.days

    return tahun, bulan, hari, total_bulan, total_hari

# Looping untuk mengulang program hitung umur sampai user menekan t
while True:
    # Menampilkan judul program
    print("PROGRAM HITUNG UMUR SEDERHANA")
    print("="*50)

    # Mengambil input tanggal lahir dari user
    tahun_lahir = int(input("Masukan tahun lahir (0-2024): "))
    bulan_lahir = int(input("Masukan bulan lahir (1-12): "))
    hari_lahir = int(input("Masukan hari lahir (1-31): "))
    print("="*50)
    print("")

    # Membuat objek tanggal lahir
    tanggal_lahir = datetime(tahun_lahir, bulan_lahir, hari_lahir)

    # Memanggil fungsi hitung_umur untuk menghitung umur
    umur_tahun, umur_bulan, umur_hari, total_bulan, total_hari = hitung_umur(tanggal_lahir)

    # Menampilkan hasil umur
    if umur_tahun < 10:
        print("Kamu masih anak-anak.")
    elif umur_tahun < 20:
        print("Kamu seorang remaja.")
    elif umur_tahun < 60:
        print("Kamu sudah dewasa.")
    else:
        print("Wah sudah sepuh.")
    print("-"*50)
    print("Umur anda adalah {} tahun, {} bulan, {} hari.".format(umur_tahun, umur_bulan, umur_hari))
    print("Umur anda dalam bulan adalah {} bulan.".format(total_bulan))
    print("Umur anda dalam hari adalah {} hari.".format(total_hari))
    print("-"*50)

    # Meminta user untuk mengulangi program atau tidak
    ulangi = input("Apakah anda ingin menghitung umur lagi? (y/t): ").lower()
    if ulangi != "y":
        print("Terimakasih telah menggunakan program ini.")
        break
    print("-"*50)
    print("")
