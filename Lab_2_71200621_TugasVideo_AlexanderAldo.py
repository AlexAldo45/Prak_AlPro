#Nama : Alexander Aldo Siandica Nugroho
#Universitas Kristen Duta Wacana

"""
Nina mempunyai adik yang sedang kesulitan mengerjakan tugas matematikanya
disaat nina melihat soal adiknya ternyata banyak soal segitiga dan persegi panjang.
Buatlah program yang membantu adiknya Nina agar adiknya mudah dalam mencari luas dan kelilingnya.
Catatan rumus :

Segitiga
Luas = 1/2 * a *t (a = alas, t = tinggi)
Keliling = s + s + s (s = sisi)
Persegi panjang
Luas = p * l (p = panjang, l = Lebar)
Keliling = (p + l)*2

"""

"""
Input:Memasukkan angka atau soal yang tertera
Proses: Penghitungan soalnya menurut rumus yang tertera diatas tergantung luas atau keliling yang dicari
Output: luas atau keliling yang dicari dari bangun datar yang dipilih

"""
while True:
    print("Selamat datang di mesin hitung bangun datar")
    print("Silahkan pilih bangun datar yang ingin dihitung")
    print("[1 = Segitiga]", "[2 = Persegi panjang]")
    pilih = input("Masukkan angka diatas untuk menghitung bangun datarnya : ")
    betul = ['1', '2']
    if pilih in betul:

        loop = True

        while loop:
            pilih_2 = input('Akan menghitung [L = Luas] / [K = Keliling]? Ketik L/K : ')
            if pilih == '1':
                milih = ['l', 'L']
                milih_2 = ['K', 'k']
                if pilih_2 in milih:
                    alas_seg = float(input("Masukkan alasnya : "))
                    ting_seg = float(input("Masukkan tingginya : "))
                    luas_seg = alas_seg * ting_seg / 2
                    print("Luas segitiga adalah", luas_seg)
                    loop = False
                elif pilih_2 in milih_2:
                    sisi_1 = float(input('Masukkan sisi 1 segitiga : '))
                    sisi_2 = float(input('Masukkan sisi 2 segitiga : '))
                    sisi_3 = float(input('Masukkan sisi 3 segitiga : '))
                    kel_seg = sisi_1 + sisi_2 + sisi_3
                    print("Keliling segitiga adalah", kel_seg)
                    loop = False
            elif pilih == '2':
                milih = ['l', 'L']
                milih_2 = ['K', 'k']
                if pilih_2 in milih:
                    pan_per = float(input("Masukkan panjang persegi panjang : "))
                    leb_per = float(input("Masukkan lebar persegi panjang : "))
                    luas_per = pan_per * leb_per
                    print("Luas persegi panjang adalah", luas_per)
                    loop = False
                elif pilih_2 in milih_2:
                    pan_per_1 = float(input("Masukkan panjang persegi panjang : "))
                    leb_per_1 = float(input("Masukkan lebar persegi panjang : "))
                    kel_per = (pan_per_1 + leb_per_1) * 2
                    print("Keliling Persegi panjang adalah", kel_per)
                    loop = False