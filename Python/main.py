# Meminta pengguna memasukan jumlah baris
jumlah_baris = int(input("Masukan jumlah baris: "))

# Looping untuk setiap baris
for i in range(jumlah_baris + 1):
    # Looping untuk mencetak spasi sebelum bintang
    for j in range(jumlah_baris - i):
        print(" ", end="")
    # Looping untuk mencetak bintang pada setiap baris
    for j in range(2*i - 1):
        print("*", end="")
    # pindah garis berikutnya
    print()