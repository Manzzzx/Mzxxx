# Meminta input jumlah mahasiswa dari user
jml = int(input("Masukan jumlah mahasiswa :"))

# Membuat list kosong untuk menampung data mahasiswa
data_mahasiswa = []

# Melakukan perulangan untuk setiap mahasiswa
for i in range(jml):
    # Menampilkan pesan data ke mahasiswa
    print("data ke mahasiswa ->",i+1)
    # Mengambil input nama, umur, dan jenis kelamin
    nama = input("Masukan nama :")
    umur = int(input("Masukan umur :"))
    jk   = input("Masukan jenis kelamin :")

    # Menambahkan data mahasiswa ke dalam list data_mahasiswa
    data_mahasiswa.append({"nama":nama, "umur":umur, "jk": jk})

# Menampilkan tabel header
print("-"*50)
print(f"{'NAMA':<20} {'UMUR':<15} {'JENIS KELAMIN':<15}")
print("-"*50)

# Menampilkan data mahasiswa
for i in data_mahasiswa:
    print(f"{i['nama']:<20} {i['umur']:<15} {i['jk']:<15}")

# Menampilkan garis bawah
print("-"*50)
