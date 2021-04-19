# Nama : Alexander Aldo Siandica Nugroho
# Universitas Kristen Duta Wacana

'''
Dina adalah pencatat menu di suatu warung makanan, dia terlihat kesulitan karena setiap
mencatat harus di kertas dan itu menghabiskan kertas. Bantulah Dina untuk membuatkannya program
mencatat menu makanan dan menu makanan itu di simpan sebagai menu_makanan.txt agar 
Dina bisa mengirimkan ke koki di warung itu.

catatan : 
daftar makan = 1. Nasi Goreng 2. Mie Goreng 3. Mie Rebus 4. Nasi Omelet
daftar minum = 1. Es/Panas Jeruk 2. Es/Panas Teh 3. Es Jus Jambu 4. Es Jus Pepaya
daftar cemilan = 1. Tempe Goreng 2. Pisang goreng
'''
'''
Input   : User memasukkan daftar menu makanan, minuman dan cemilan, dan menambakan pilihan apakah ada menu tambahan lagi. input yaitu ya atau tidak
Proses  : setelah memasukkan semua menu dan tambahan menu source code memproses semua data dan memindahkannya ke file .txt
Output  : file.txt dan print hasil menu di python
'''

file_teks = open("C:\\Users\\M S I\\OneDrive\\Desktop\\Menu_Makanan\\Daftar_Makanan.txt", "w")
print("="*5, "SELAMAT DATANG DI PENCATAT MENU MAKANAN", "="*5)
makan = "Makanan : "
minum = "Minuman : "
cemilan = "Cemilan : "

while True:
    print("="*5, "Silahkan Ketik Pesanan", "="*5)
    print("Makanan :\n1. Nasi Goreng\n2. Mie Goreng\n3. Mie Rebus\n4. Nasi Omelet")
    makan2 = str(input("Masukkan makanan beserta jumlahnya : "))
    print("Minuman :\n2. Es/Panas Jeruk\n2. Es/Panas Teh\n3. Es Jus Jambu\n4. Es Jus Pepaya")
    minum2 = str(input("Masukkan minuman beserta jumlahnya : "))
    print("Cemilan :\n1. Tempe Goreng\n2. Pisang Goreng")
    cemilan2 = str(input("Masukkan cemilan beserta jumlahnya : "))
    makan += makan2
    minum += minum2
    cemilan += cemilan2

    print("Menu yang dipilih")
    print(makan, "\n", minum, "\n", cemilan)
    pilih = int(input("Apakah ingin menambah menu? (1 = ya / 2 = tidak) : "))
    if pilih == 2:
        file_teks.write(makan)
        file_teks.write(minum)
        file_teks.write(cemilan)
        file_teks.close()
        break
    elif pilih == 1:
        makan3 = str(input("Ketik yang ingin ditambah makanan : "))
        makan += makan3
        minum3 = str(input("Ketik yang ingin ditambah minuman : "))
        minum += minum3
        cemilan3 = str(input("Ketik yang ingin ditambah cemilan : "))
        file_teks.close()
        break
