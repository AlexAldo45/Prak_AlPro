#Nama : Alexander Aldo Siandica Nugroho
#Universitas Kristen Duta Wacana

'''
Buatlah sebuah program yang dapat menghitung luas dan keliling lingkaran
dengan memakai fungsi atau def
Catatan :
luas = 3.14*jari**2
keliling = 3.14*jari*2

def hitung_keliling():

def hitung_luas():
'''
'''
Input : Berupa angka dan jari-jari
Proses : menghitung inputan user sesuai rumus diatas
Output : Hasil dari luas atau keliling pilihan user
'''
def hitung_luas():
    print("Menghitung luas lingkaran")
    jari = float(input("Ketik jari-jarinya : "))
    luas = 3.14 * (jari**2)
    print("Luas lingkaran adalah :", luas)

def hitung_keliling():
    print("Menghitung keliling lingkaran")
    jari_2 = float(input("Ketik jari-jarinya : "))
    keliling = 3.14 * jari_2 * 2
    print("Keliling lingkaran adalah :", keliling)

#Program Utama
while True:
    print('=' * 15, "Menghitung lingkaran", '=' * 15)
    print("1. Luas lingkaran")
    print("2. Keliling lingkaran")

    pilihan_user = input("Ketik pilihan anda (1/2) : ")
    if pilihan_user == '1':
        hitung_luas()
    elif pilihan_user == '2':
        hitung_keliling()
    else:
        print("Pilihan anda salah, silahkan masukkan lagi!!!")