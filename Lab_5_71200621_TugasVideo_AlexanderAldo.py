#Nama : Alexander Aldo Siandica Nugroho
#Universitas Kristen Duta Wacana

'''
Buatlah sebuah program yang dapat menghitung Volume dan Luas permukaan 
dari Kubus dan Balok, dengan tambahan memakai password untuk membuka program
menghitung tersebut
catatan :
password = 'alex' dan 'aldo'

Balok   : Luas permukaan = 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)
        : volume = panjang * lebar * tinggi
Kubus   : Luas permukaan = 6 * sisi **2
        : Volume = sisi **3
'''
'''
Input : Berupa masukkan password, pilihan balok atau kubus, dan pilihan volume atau luas permukaan
Proses : program menghitung pilihan user sesuai rumus
Output : hasil dari pilihan user yaitu luas permukaan dan volume
'''

verifikasi = input("Masukkan password anda : ")
while True:
    password = ['alex', 'aldo']
    if verifikasi in password:
        print("Menghitung Bangun Ruang")
        print("1. Kubus")
        print("2. Balok")
        try:
            pilihan_user = int(input("Masukkan bangun ruang yang ingin di hitung (1/2) : "))
            rumus = str.lower(input("Ingin menghitung [Volume = V] atau [Luas Permukaan = L]? Tulis (V/L) : "))
            if pilihan_user == 1:
                if rumus == 'l':
                    sisi = int(input("Masukkan sisinya : "))
                    rum_luas_kub = 6 * (sisi**2)
                    print("Luas permukaan Kubus adalah :", rum_luas_kub)
                elif rumus == 'v':
                    sisi_2 = int(input("Masukkan sisinya : "))
                    rum_vol_kub = sisi_2**3
                    print("Volume Kubus adalah :", rum_vol_kub)
            elif pilihan_user == 2:
                if rumus == 'l':
                    panjang = int(input("Masukkan panjangnya : "))
                    lebar = int(input("Masukkan lebarnya : "))
                    tinggi = int(input("Masukkan tingginya : "))
                    rum_luas_bal = 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)
                    print("Luas permukaan Balok adalah :", rum_luas_bal)
                elif rumus == 'v':
                    panjang_2 = int(input("Masukkan panjangnya : "))
                    lebar_2 = int(input("Masukkan lebarnya : "))
                    tinggi_2 = int(input("Masukkan tingginya : "))
                    rum_vol_bal = panjang_2 * lebar_2 * tinggi_2
                    print("Volume Balok adalah :", rum_vol_bal)
        except:
            print("Input anda salah")
            continue
    else:
        print("Passwor yang anda masukkan salah")
        verifikasi = input("Masukkan password anda : ")