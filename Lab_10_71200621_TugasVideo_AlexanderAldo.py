# Nama : Alexander Aldo Siandica Nugroho
# Universitas Kristen Duta Wacana

'''
Dina mempunyai sebuah toko buku yang mempunyai beberapa barang
suatu hari Dina ingin mengupgrade tulisan harga setiap barang
dari kertas menjadi program.
Bantulah Dina untuk membuat program yang dapat menampilkan harga 
barang sesuai harganya memakai Dictionary

Catatan :
Barang dibagi menjadi 2:
    - Buku = 1. Buku Gambar A3 2. Buku Gambar A4 3. Buku Tulis 4. Buku Tegak Bersambung 5. Buku Kotak-Kotak 6. Buku Catatan Mulus
        Harga = 1 : 5000, 2 : 3500, 3 : 2500, 4 : 3000, 5 : 3500, 6 : 4000
    - Alat Tulis = 7. Pensil 8. Penghapus 9. Penggaris 10. Bolpoin 11. Tipe X 12. Spidol 13. Rautan
        Harga = 7 : 1500, 8 : 1000, 9 : 3000, 10 : 2500, 11 : 5000, 12 : 3000, 13 : 1500

'''
'''
Input : Pilihan user memilih Buku atau alat tulis, nama barang yang ingin diketahui harganya
Proses : program memilah pilihan user buku arau alat tulis, program menentukan harga barang sesuai inputan user
Ouput : program mengprint hasil pilihan user (Harga, Nama barang pilihan user)
'''

buku = {1 : 'Buku Gambar A3', 2 : 'Buku Gambar A4', 3 : 'Buku Tulis', 4 : 'Buku Tegak Bersambung', 5 : 'Buku Kotak-Kotak', 6 : 'Buku Catatan Mulus'}
alat_tulis = {7 : 'Pensil', 8 : 'Penghapus', 9 : 'Penggaris', 10 : 'Bolpoin', 11 : 'Tipe X', 12 : 'Spidol', 13 : 'Rautan'}
harga_buku = {1 : '5000', 2 : '3500', 3 : '2500', 4 : '3000', 5 : '3500', 6 : '4000'}
harga_alat_tulis = {7 : '1500', 8 : '1000', 9 : '3000', 10 : '2500', 11 : '5000', 12 : '3000', 13 : '1500'}

while True:
    print("="*5, "Selamat Datang di Mesin Cari", "="*5)
    print("Silahkan Pilih Barang yang Ingin dicari Harganya\n1. Buku\n2. Alat Tulis")
    user1 = int(input("Pilihan Anda : "))
    if user1 == 1:
        print("1. Buku Gambar A3\n2. Buku Gambar A4\n3. Buku Tulis\n4. Buku Tegak Bersambung\n5. Buku Kotak-Kotak\n6. Buku Catatan Mulus")
        barang = int(input("Ketik Nomor barang : "))
        print("Pilihan :", buku.pop(barang))
        print("Harga :", harga_buku.pop(barang))
    elif user1 == 2:
        print("7. Pensil\n8. Penghapus\n9. Penggaris\n10. Bolpoin\n11. Tipe X\n12. Spidol\n13. Rautan")
        barang2 = int(input("Ketik Nomor barang : "))
        print("Pilihan :", alat_tulis.pop(barang2))
        print("Harga :", harga_alat_tulis.pop(barang2))
    else:
        print("Input Anda Salah")
