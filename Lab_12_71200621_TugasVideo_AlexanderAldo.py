# Nama : Alexander Aldo Siandica Nugroho
# Universitas Kristen Duta Wacana

'''
Fahri adalah seoarang anak sma yang mendapatkan soal
irisan dan komplemen dari gurunya. Untuk memudahkan dia
mengerjakan soal tersebut Fahri ingin membuat program yang
dapat mencari irisan dan komplomen tapi dia tidak bisa coding.
Bantulah Fahri dalam membuat program tersebut

Catatan : Harus menggunakan Set
'''
'''
Input : jumlah banyak angka yg ingin dimasukkan user, memasukkan angka yg ingin dicari, memasukkan pilihan menu irisan atau komplemen
Proses : program melakukan tugas sesuai inputan user
Output : program mengeprint hasil jadi dari inputan hasil
'''

print("="*5, "Program Operasi Set", "="*5)
user_1 = int(input("== Masukkan jumlah angka 1 : "))
user_2 = int(input(">> Masukkan jumlah angka 2 : "))

print("1. Irisan\n2. Komplemen")
pilih_user = int(input("Masukkan pilihan anda (1/2) : "))
kosong = {' '}
kosong_2 = {' '}

for i in range (user_1):
    user_input1 = int(input("== Masukkan angka 1 : "))
    kosong.add(user_input1)
for x in range (user_2):
    user_input2 = int(input(">> Masukkan angka 2 : "))
    kosong_2.add(user_input2)

kosong.remove(' ')
kosong_2.remove(' ')

if pilih_user == 1:
    a = kosong.intersection(kosong_2)
    if a == set():
        print("Tidak ada Irisan")
    else:
        print("Hasilnya adalah", a)
elif pilih_user == 2:
    b = kosong.symmetric_difference(kosong_2)
    if b == set():
        print("Tidak ada Komplemen")
    else:
        print("Hasilnya adalah", b)