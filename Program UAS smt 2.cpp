#include <iostream>
#include <string>

using namespace std;


const string namaKereta[] = {"Argo Bromo", "Argo Lawu", "Parahyangan"};
const int hargaKelas[] = {100000, 80000, 50000};  
const string namaKelas[] = {"Eksekutif", "Bisnis", "Ekonomi"};

const string namaJurusan[] = {"JKT-SBY", "JKT-SMG", "JKT-BDN", "JKT-BALI"};
const int biayaTambahan[] = {40000, 30000, 20000, 50000};


int hitungTotalHarga(int hargaKelas, int biayaJurusan, int jumlahTiket) {
    int totalHarga = (hargaKelas + biayaJurusan) * jumlahTiket;
    if (jumlahTiket >= 10) {
        totalHarga *= 0.75;  
    } else if (jumlahTiket >= 5) {
        totalHarga *= 0.90;  
    }
    return totalHarga;
}

int main() {
    int kodeKereta, kodeKelas, kodeJurusan, jumlahTiket;
    char ulang;

    do {
        cout << "Masukan data : ";
        char data;
        cin >> data;
        cout << "Masukkan Kode Kereta : ";
        char kodeKeretaChar;
        cin >> kodeKeretaChar;


        switch (kodeKeretaChar) {
        case 'B': kodeKereta = 0; break;
        case 'L': kodeKereta = 1; break;
        case 'P': kodeKereta = 2; break;
        default: cout << "Kode kereta tidak valid" << endl; return 1;
    }

            cout << "Nama Kereta : " << namaKereta[kodeKereta] << endl;

            cout << "Masukkan Pilihan Kelas : ";
            cin >> kodeKelas;
            if (kodeKelas < 1 || kodeKelas > 3) {
            cout << "Kode kelas tidak valid" << endl;
            return 1;
            }
            
            kodeKelas--;  
            cout << "Nama Kelas : " << namaKelas[kodeKelas] << ", Harga : Rp. " << hargaKelas[kodeKelas] << endl;
            cout << "Masukkan Pilihan Jurusan (JKT-SBY, JKT-SMG, JKT-BDN, JKT-BALI) : ";
            string kodeJurusanStr;
            cin >> kodeJurusanStr;

    if (kodeJurusanStr == "JKT-SBY") {
        kodeJurusan = 0;
    } else if (kodeJurusanStr == "JKT-SMG") {
        kodeJurusan = 1;
    } else if (kodeJurusanStr == "JKT-BDN") {
        kodeJurusan = 2;
    } else if (kodeJurusanStr == "JKT-BALI") {
        kodeJurusan = 3;
    } else {
        cout << "Kode jurusan tidak valid" << endl;
        return 1;
    }

    cout << "Nama Jurusan : " << namaJurusan[kodeJurusan] << ", Biaya Tambahan: Rp. " << biayaTambahan[kodeJurusan] << endl;


    cout << "Masukkan jumlah tiket : ";
    cin >> jumlahTiket;
    if (jumlahTiket <= 0) {
        cout << "Jumlah tiket tidak valid" << endl;
        return 1;
    }


    int hargaDasar = hargaKelas[kodeKelas];
    int biayaJurusan = biayaTambahan[kodeJurusan];
    int totalHarga = hitungTotalHarga(hargaDasar, biayaJurusan, jumlahTiket);


    cout << "\n        PT KAI BREBES        \n";
    cout << "Data Ke           : " << data << "\n";
    cout << "Kode Kereta       : " << kodeKeretaChar << "\n";
    cout << "Nama Kereta       : " << namaKereta[kodeKereta] << "\n";
    cout << "Kelas Pilihan     : " << kodeKelas + 1 << "\n";
    cout << "Nama Kelas        : " << namaKelas[kodeKelas] << "\n";
    cout << "Harga             : Rp. " << hargaDasar << "\n";
    cout << "Jurusan           : " << namaJurusan[kodeJurusan] << "\n";
    cout << "Biaya Tambahan    : Rp. " << biayaJurusan << "\n";
    cout << "Harga Tiket       : Rp. " << hargaDasar + biayaJurusan << "\n";
    cout << "Discount          : Rp. " << (jumlahTiket >= 10 ? 0.25 * (hargaDasar + biayaJurusan) * jumlahTiket : jumlahTiket >= 5 ? 0.1 * (hargaDasar + biayaJurusan) * jumlahTiket : 0) << "\n";
    cout << "Total Bayar       : Rp. " << totalHarga << "\n";

    std::cout << "\nIngin memilih kereta lain (y/t)? ";
    std::cin >> ulang;
    
    } while (ulang == 'y' || ulang == 'Y');

    std::cout << "\nTerimakasih...\n";
    return 0;
}
