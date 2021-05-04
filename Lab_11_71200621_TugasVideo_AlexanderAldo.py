# Nama : Alexander Aldo Siandica Nugroho
# Universitas Kristen Duta Wacana

'''
Buatlah sebuah program yang dapat mengurutkan
angka dari kecil ke besar. Dan di program
itu harus disertakan password untuk mengamankan
program tersebut

catatan :   Hasil akhir harus tuple
            dan harus diberi keterangan type 
            dari hasil program tersebut
'''
'''
Input   : user memasukkan password, memasukkan jumlah angka yang ingin di urutkan, memasukkan angka yang ingin diurutkan
Proses  : program mengecek password benar atau salah, melakukan perulangan dari jumlah angka yang dimasukkan, menambahkannya ke variabel kosong lalu mengurutkannya,
          dan mengubah menjadi tuple
Output  : mengeprint hasil yang sudah diurutkan dan mengeprint type hasil tersebut
'''

while True:
    user_password = str(input("Masukkan Passwordnya : "))
    if user_password == 'aldo' or user_password == 'alex':
        list_kosong = []
        print("="*6, "Selamat Datang di Program Pengurut Nomor", "="*6)
        try:
            user = int(input("Masukkan jumlah angka : "))
            for x in range (user):
                user_2 = int(input("Masukkan Angka : "))
                list_kosong.append(user_2)
            list_kosong.sort()
            tuple_update = tuple(list_kosong)
            print(tuple_update)
            print(type(tuple_update))
            del list_kosong[0:]
        except:
            print("Input Anda Salah")
    else:
        print("Password Anda Salah")
