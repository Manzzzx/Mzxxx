# Menampilkan menu makanan
print("|===================================|")
print("|      PROGRAM KASIR SEDERHANA      |")
print("|===================================|")
print("|       : PILIH MENU MAKANAN :      |")
print("|===================================|")
print("|Ayam Bakar                Rp.15000 |")  # Menu 1
print("|Ayam Geprek               Rp.15000 |")  # Menu 2
print("|Nasi Rendang              Rp.20000 |")  # Menu 3
print("|Nasi Pecel                Rp.10000 |")  # Menu 4
print("|Soto Ayam                 Rp.12000 |")  # Menu 5
print("|===================================|")
print("                                     ")

# Menginputkan nomor makanan dan jumlah porsi
nomer_makanan = int(input("pilih (1/2/3/4/5) :"))
jml_porsi = int(input("Berapa porsi :"))

# Proses pembelian makanan
if nomer_makanan in range(1, 6):
    # Menghitung total biaya makanan
    total_makanan = jml_porsi * [15000, 15000, 20000, 10000, 12000][nomer_makanan - 1]
    # Menampilkan total biaya makanan
    print(f"{['Ayam Bakar', 'Ayam Geprek', 'Nasi Rendang', 'Nasi Pecel', 'Soto Ayam'][nomer_makanan - 1]} {jml_porsi} Porsi Rp.{total_makanan}")
    # Menyimpan nama makanan yang dibeli
    makanan = ['Ayam Bakar', 'Ayam Geprek', 'Nasi Rendang', 'Nasi Pecel', 'Soto Ayam'][nomer_makanan - 1]
else:
    print("Menu tidak terdaftar!")

# Menampilkan menu minuman
print("                                     ")
print("|===================================|")
print("|       : PILIH MENU MINUMAN :      |")
print("|===================================|")
print("|Teh Tawar                 Rp.3000  |")  # Menu 1
print("|Kopi Susu                 Rp.8000  |")  # Menu 2
print("|Es Milo                   Rp.13000 |")  # Menu 3
print("|Lemon Tea                 Rp.8000  |")  # Menu 4
print("|Es Jeruk                  Rp.5000  |")  # Menu 5
print("|===================================|")
print("                                     ")

# Menginputkan nomor minuman dan jumlah gelas
nomer_minuman = int(input("pilih (1/2/3/4/5) :"))
jml_gelas = int(input("Berapa gelas :"))

# Proses pembelian minuman
if nomer_minuman in range(1, 6):
    # Menghitung total biaya minuman
    total_minuman = jml_gelas * [3000, 8000, 13000, 8000, 5000][nomer_minuman - 1]
    # Menampilkan total biaya minuman
    print(f"{['Teh Tawar', 'Kopi Susu', 'Es Milo', 'Lemon Tea', 'Es Jeruk'][nomer_minuman - 1]} {jml_gelas} Porsi Rp.{total_minuman}")
    # Menyimpan nama minuman yang dibeli
    minuman = ['Teh Tawar', 'Kopi Susu', 'Es Milo', 'Lemon Tea', 'Es Jeruk'][nomer_minuman - 1]
else:
    print("Menu tidak terdaftar!")

# Menghitung total pembayaran
total_semua = total_makanan + total_minuman

# Menampilkan total pembayaran
print(f"Total pembayaran Rp. {total_semua}")

# Menginputkan pembayaran
bayar = int(input("Masukan Pembayaran anda :"))

# Mengecek apakah pembayaran cukup
if bayar >= total_semua:
    kembalian = bayar - total_semua
else:
    uang_kurang = total_semua - bayar
    print("Uang yang anda bayar kurang!")
    exit()
# Menampilkan struk pembelian
print("                                     ")
print("                                     ")
print("|===================================|")
print("|          STRUK PEMBELIAN          |")
print("|===================================|")
print("  Makanan            :",makanan,"\t")
print("  Jumlah Porsi       :",jml_porsi,"\t")
print("  Minuman            :",minuman,"\t")
print("  Jumlah Gelas       :",jml_gelas,"\t")
print("  Total Pembayaran   :",total_semua,"\t")
print("  bayar              :",bayar,"\t")
print("  Kembalian          :",kembalian,"\t")
print("                                     ")
print("Terima kasih telah berbelanja disini!")

