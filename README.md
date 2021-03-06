# UAS2022
## MATA KULIAH B.PEMOGRAMAN
## NAMA     : TJOKRO WINATA
## NIM      : 312110276
## KELAS    : TI.21.A.2

### Sesuai dengan tugas UAS yang diberikan

![gambar1](ss/ss8.png)

- daftar_nilai.py berisi modul untuk tambah data, ubah data, cari data, hapus data
- view_nilai.py berisi modul untuk cetak daftar nilai, cetak hasil pencarian
- input_nilai.py berisi modul untuk input data yang diminta pengguna untuk memasukkan data
- main.py berisi program secara keseluruhan

### Projek Saya

![gambar2](ss/ss1.png)

### Beberapa penjelasan mengenai program

- program daftar_nilai.py

```python
from view.input_nilai import *

dataMahasiswa = {}


def tambah_data():
    global dataMahasiswa
    nama = input_nama()
    nim = input_nim()
    nilaiTugas = input_nilaiTugas()
    nilaiUts = input_nilaiUts()
    nilaiUas = input_nilaiUas()
    nilaiAkhir = (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
    dataMahasiswa[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
    print("\nData Berhasil Ditambahkan!")
    return dataMahasiswa

def ubah_data():
    nama = input("Masukkan Nama: ")
    if nama in dataMahasiswa.keys():
        nim = input_nim()
        nilaiTugas = input_nilaiTugas()
        nilaiUts = input_nilaiUts()
        nilaiUas = input_nilaiUas()
        nilaiAkhir = (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
        dataMahasiswa[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
        print("\nData Berhasil Di Update!")
    else:
        print("Data tidak ditemukan!")


def hapus_data():
    nama = input("Masukkan Nama:  ")
    if nama in dataMahasiswa.keys():
        del dataMahasiswa[nama]
        print("Data",nama, "Telah dihapus!")
    else:
        print("Data Mahasiswa Tidak Ada".format(nama))
```
- program view_nilai.py

```python
from model.daftar_nilai import *


def cetak_daftar_nilai():
    if dataMahasiswa.items():
        print("\n                      DAFTAR NILAI MAHASISWA                    ")
        print("==================================================================")
        print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
        print("==================================================================")
        i = 0
        for x in dataMahasiswa.items():
            i += 1
            print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
        print("==================================================================")
    else:
        print("\n                      DAFTAR NILAI MAHASISWA                    ")
        print("==================================================================")
        print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
        print("==================================================================")
        print("|                          TIDAK ADA DATA!                       |")
        print("==================================================================")


def cetak_hasil_pencarian():
    nama = input("Masukkan Nama        : ")
    if nama in dataMahasiswa.keys():
        print("\n                   DAFTAR NILAI MAHASISWA                   ")
        print("==============================================================")
        print("|     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir  |")
        print("==============================================================")
        print("| {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6}  |".format(nama, dataMahasiswa[nama][0], dataMahasiswa[nama][1], dataMahasiswa[nama][2], dataMahasiswa[nama][3], dataMahasiswa[nama][4]))
        print("==============================================================")
    else:
        print("Datanya {0} Tidak Ada ".format(nama))
```

- Program input_nilai.py

```python
def input_nama():
    global nama
    nama = input("Masukkan Nama        : ")
    return nama


def input_nim():
    global nim
    nim = input("Masukkan NIM         : ")
    return nim


def input_nilaiTugas():
    global nilaiTugas
    nilaiTugas = int(input("Masukkan Nilai Tugas : "))
    return nilaiTugas


def input_nilaiUts():
    global nilaiUts
    nilaiUts = int(input("Masukkan Nilai UTS   : "))
    return nilaiUts


def input_nilaiUas():
    global nilaiUas
    nilaiUas = int(input("Masukkan Nilai UAS   : "))
    return nilaiUas
```

- Dan yang terakhir ini untuk program main.py

```python
from view.view_nilai import *


def menu():
    print('=====================================')
    print('Input Data Nilai Mahasiswa'.center(40))
    print('=====================================')
    print('|    1. Tambah Data                 |')
    print('|    2. Cari Data                   |')
    print('|    3. Tampilkan Data              |')
    print('|    4. Ubah Data                   |')
    print('|    5. Hapus Data                  |')
    print('|    6. Selesai                     |')
    print('=====================================')


while True:
    menu()
    choose = input('Pilih Menu  : ')

    if choose == '1':
        tambah_data()
        input('Untuk kembali, tekan enter')

    elif choose == '2':
        cetak_hasil_pencarian()
        input('Untuk kembali, tekan enter')

    elif choose == '3':
        cetak_daftar_nilai()
        input('Untuk kembali, tekan enter')

    elif choose == '4':
        ubah_data()
        input('Untuk kembali, tekan enter')

    elif choose == '5':
        hapus_data()
        input('Untuk kembali, tekan enter')

    elif choose == '6':
        exit()

    else:
        print("Menu yang dicari tidak ditemukan, Silahkan pilih menu yang tersedia")
```

- Diatas merupakan beberapa penjelasan mengenai program yang kita jalankan kali ini

### Keterangan
- Berikut adalah tampilan setelah di run

![gambar3](ss/ss2.png)

- untuk memulai program dapat dengan menekan angka sesuai perintah, sebagi contoh kita tekan 1 untuk menambah data
- Dan isi lah keterangan sesuai perintah

![gambar4](ss/ss4.png)

- Dan tekan angka 2 apabila ingin mencari serta melihat data

![gambar5](ss/ss3.png)

- Apabila ingin mengubah tekan 4 , dan isi sesuai keriteria data tersebut
- Sebagai contoh saya disini menambahkan ADIT

![gambar6](ss/ss5.png)

- Tekan angka 5 jika ingin menghapus data
- Disini saya menghapus data ADIT

![gambar7](ss/ss6.png)

- Dan apabila sudah selesai , anda bisa menekan angka 6 maka data selesai dibuat

![gambar8](ss/ss7.png)

### Mungkin sekian yang dapat saya jelaskan
## TERIMA KASIH !

