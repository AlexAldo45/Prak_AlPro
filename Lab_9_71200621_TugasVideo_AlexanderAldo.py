# Nama : Alexander Aldo Siandica Nugroho
# Universitas Kristen Duta Wacana

'''
Suatu hari kamu melihat Mama kamu kesulitan dalam mengingat daftar belanjanya
setiap memakai kertas untuk menulisnya dia selalu ketinggalan,
bantulah mama kamu dalam membuat program mencatat list belanja
mama anda menggunakan List.

catatan :
Bagi List belanja jadi 2 yaitu list belanja kering dan basah
'''

'''
Input : menambah data list belanja, menampilan list belanja, menghapus list  belanja, keluar, pilihan kering atau basah
Proses : program menampilan, user memilih, menambahkan inputan user ke dalam variabel list, menampilkan data dan keluar
Output : Data list belanja, tampilan yang sudah dihapus
'''

daftar_belanja_kering = []
daftar_belanja_basah = []

while True:
    print("="*5, "Program List Belanja", "="*5)
    print("1. Tambah List Belanja\n2. List Belanja\n3. Menghapus List Belanja\n4. Keluar")
    user_pilih = int(input("Masukkan Pilihan Anda [1-4] : "))
    if user_pilih == 1:
        user_pilih2 = int(input("List Belanja 1 = Kering atau 2 = Basah ? [1/2] : "))
        if user_pilih2 == 1:
            jumlah = int(input("Banyak List : "))
            for x in range (jumlah):
                kering = str(input("Masukkan List Belanja Kering : "))
                daftar_belanja_kering.append(kering)
        elif user_pilih2 == 2:
            jumlah2 = int(input("Banyak List : "))
            for x in range (jumlah):
                basah = str(input("Masukkan List Belanja Basah : "))
                daftar_belanja_basah.append(basah)
        else:
            print("Input Anda Salah")
    
    elif user_pilih == 2:
        print("Daftar Belanja Kering", daftar_belanja_kering)
        print("Daftar Belanja Basah", daftar_belanja_basah)
    
    elif user_pilih == 3:
        user_pilih3 = int(input("List Belanja 1 = Kering atau 2 = Basah ? [1/2] : "))
        if user_pilih3 == 1:
            banyak_hapus = int(input("List Banyak di Hapus : "))
            print(daftar_belanja_kering)
            for x in range (banyak_hapus):
                hapus = str(input("Ketik list yang dihapus : "))
                daftar_belanja_kering.remove(hapus)
                print("Berhasil dihapus")
        elif user_pilih3 == 2:
            banyak_hapus = int(input("List Banyak di Hapus : "))
            print(daftar_belanja_basah)
            for x in range (banyak_hapus):
                hapus2 = str(input("Ketik list yang dihapus : "))
                daftar_belanja_basah.remove(hapus2)
                print("Berhasil dihapus")
    
    elif user_pilih == 4:
        print("Selamat Tinggal")
        break

    else:
        print("input anda salah")