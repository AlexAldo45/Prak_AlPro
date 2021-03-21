#Nama : Alexander Aldo Siandica Nugroho
#Universitas Kristen Duta Wacana

'''
BMI (Body Mass Index) adalah  salah satu cara untuk menentukan apakah seseorang 
bertubuh gemuk, langsing, atau kurus berdasarkan hasil bagi massa tubuh (kilogram) 
dengan tinggi badan (meter) kuadrat.

Nilai BMI di bawah 18.5 berarti terlalu kurus, langsing/sehat pada rentang 18.5 s.d 
di bawah 25, 25+ tergolong gemuk.

Buatlah sebuah program yang menanyakan berapa berat badan seseoarang (dalam kg), dan berapa tingginya (dalam cm, 1m = 100 cm), 
kemudian hitung nilai BMInya. Setelah nilai BMI didapatkan, cetak nilai BMI dan 
apakah orang tersebut termasuk kurus, langsing, atau gemuk. Lihat contoh output berikut untuk lebih jelasnya.

catatan:
tinggi badan/100
rumus BMI = berat badan / (tinggi badan * tinggi badan)
'''

'''
input : berat badan, tinggi badan, keluar dari program atau tidak
proses : program menghitung rumus BMI yang tertera diatas
output : hasil dari BMI, hasil apakah langsing, kurus atau gemuk
'''

while True:
    print("="*10, "Selamat datang di penghitung BMI", "="*10)
    print("="*10, "Silahkan masukkan data anda", "="*10)
    berat_badan = float(input("Masukkan berat badan anda (kg) : "))
    tinggi_badan = float(input("Masukkan tinggi badan anda (cm) : "))
    tinggi_badan_2 = tinggi_badan/100
    bmi = berat_badan / (tinggi_badan_2 * tinggi_badan_2)
    print("Nilai BMI anda adalah", bmi)
    if bmi < 18.5:
        print("Anda tergolong berbadan kurus")
        try:
            keluar = int(input("Apakah anda ingin keluar (1 = Ya / 2 = Tidak) ? : "))
            if keluar == 1:
                break
            elif keluar ==2:
                continue
        except:
            print("Input anda salah")
            continue
    elif bmi < 25:
        print("Anda tergolong berbadan langsing")
        try:
            keluar = int(input("Apakah anda ingin keluar (1 = Ya / 2 = Tidak) ? : "))
            if keluar == 1:
                break
            elif keluar ==2:
                continue
        except:
            print("Input anda salah")
            continue
    else:
        print("Anda tergolong berbadan gemuk")
        try:
            keluar = int(input("Apakah anda ingin keluar (1 = Ya / 2 = Tidak) ? : "))
            if keluar == 1:
                break
            elif keluar ==2:
                continue
        except:
            print("Input anda salah")
            continue
