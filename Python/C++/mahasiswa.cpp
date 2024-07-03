// #include <iostream>
// #include <string>

// int main() {
//     // Deklarasi variabel untuk menyimpan data biodata mahasiswa
//     std::string nama;
//     std::string nim;
//     std::string fakultas;
//     std::string jurusan;
//     std::string kotaAsal;
//     std::string alamat;

//     // Meminta inputan dari pengguna
//     std::cout << "Masukkan Nama      : ";
//     std::getline(std::cin, nama);
    
//     std::cout << "Masukkan NIM       : ";
//     std::getline(std::cin, nim);
    
//     std::cout << "Masukkan Fakultas  : ";
//     std::getline(std::cin, fakultas);
    
//     std::cout << "Masukkan Jurusan   : ";
//     std::getline(std::cin, jurusan);
    
//     std::cout << "Masukkan Kota Asal : ";
//     std::getline(std::cin, kotaAsal);
    
//     std::cout << "Masukkan Alamat    : ";
//     std::getline(std::cin, alamat);

//     // Menampilkan data biodata mahasiswa
//     std::cout << "\nBiodata Mahasiswa    :\n";
//     std::cout << "Nama                  : " << nama << "\n";
//     std::cout << "NIM                   : " << nim << "\n";
//     std::cout << "Fakultas              : " << fakultas << "\n";
//     std::cout << "Jurusan               : " << jurusan << "\n";
//     std::cout << "Kota Asal             : " << kotaAsal << "\n";
//     std::cout << "Alamat                : " << alamat << "\n";

//     return 0;
// }

#include <iostream>
#include <string>

int main() {
    std::string nama, nim, fakultas, jurusan, kotaAsal, alamat;

    std::cout << "Masukkan Nama      : ";
    std::getline(std::cin, nama);
    std::cout << "Masukkan NIM       : ";
    std::getline(std::cin, nim);
    std::cout << "Masukkan Fakultas  : ";
    std::getline(std::cin, fakultas);
    std::cout << "Masukkan Jurusan   : ";
    std::getline(std::cin, jurusan);
    std::cout << "Masukkan Kota Asal : ";
    std::getline(std::cin, kotaAsal);
    std::cout << "Masukkan Alamat    : ";
    std::getline(std::cin, alamat);

    std::cout << "\nBiodata Mahasiswa:\n"
              << "Nama       : " << nama << "\n"
              << "NIM        : " << nim << "\n"
              << "Fakultas   : " << fakultas << "\n"
              << "Jurusan    : " << jurusan << "\n"
              << "Kota Asal  : " << kotaAsal << "\n"
              << "Alamat     : " << alamat << "\n";

    return 0;
}
