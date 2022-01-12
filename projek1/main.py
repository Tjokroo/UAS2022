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
        print("Menu yang dicari tidak dapat ditemukan, Silahkan pilih menu yang tersedia")
