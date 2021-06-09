# Nama : Alexander Aldo Siandica Nugroho
# Universitas Kristen Duta Wacana

'''
Buatlah sebuah program perhitungan yang terdiri dari pertambahan, pengurangan,
pembagian, dan penjumlahan.

Catatan : Gunakan Rekursif untuk source codenya

'''
'''
Input : input user memilih tambah, bagi, kali, dan kurang. memasukkan angka yang ingin dihitung ada 2
Proses : program memilih pilihan user, menghitung sesuai pilihan user
Output : mencetak hasil dari pilihan user
'''

def tambah(angka1, angka2):
    try:
        return (angka1 + angka2)
    except:
        print("Input Salah")

def kali(angka3, angka4):
    try:
        return (angka3 * angka4)
    except:
        print("Input Salah")

def bagi(angka5, angka6):
    try:
        return (angka5 / angka6)
    except:
        print("Input Salah")

def kurang(angka7, angka8):
    try:
        return (angka7 - angka8)
    except:
        print("Input Salah")

while True:
    print("Selamat Datang di Mesin Hitung")
    print("1. Tambah\n2. Bagi\n3. Kurang\n4. kali")
    try:
        user = int(input("Pilih yang ingin di hitung : "))
        if user == 1:
            a1 = int(input("Masukkan angka 1 : "))
            b1 = int(input("Masukkan angka 2 : "))
            print("Hasilnya Adalah :")
            print(tambah(a1, b1))
        elif user == 2:
            a2 = int(input("Masukkan angka 1 : "))
            b2 = int(input("Masukkan angka 2 : "))
            print("Hasilnya Adalah :")
            print(bagi(a2, b2))
        elif user == 3:
            a3 = int(input("Masukkan angka 1 : "))
            b3 = int(input("Masukkan angka 2 : "))
            print("Hasilnya Adalah :")
            print(kurang(a3, b3))
        elif user == 4:
            a4 = int(input("Masukkan angka 1 : "))
            b4 = int(input("Masukkan angka 2 : "))
            print("Hasilnya Adalah :")
            print(kali(a4, b4))
        else:
            print("Input Anda Salah")
    except:
        print("Input Anda Salah")
