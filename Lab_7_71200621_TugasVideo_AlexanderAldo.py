#Nama : Alexander Aldo Siandica Nugroho
#Universitas Kristen Duta Wacana

'''
Alex adalah orang yang suka mengubah-ubah huruf dari tulisan kecil menjadi besar
dan tulisan besar menjadi kecil, biasanya alex membuatnya manual karena tidak tau cara yang cepat.
Sebagai teman yang baik bantulah alex untuk membuat program yang dapat membantu masalahnya.

catatan:
contoh = HaLo sEmUa, menjadi, hAlO SeMuA
'''
'''
Input :     Tulisan user, input keluar dari program atau tidak
Proses :    Berulang menganalisis tulisan itu apakah besar atau kecil, mengubah tulisan itu menjadi kecil atau besar, 
            memasukannya ke variabel tulisan nya yang baru dan mengeprint
Output :    Hasil yang sudah diubah tulisannya menjadi besar atau kecil
'''

while True:
    print("="*5, "Program mengubah huruf besar menjadi kecil dan huruf kecil menjadi besar", "="*5)
    huruf = str(input("Masukkan tulisan anda : "))
    kata_baru = ""
    for x in huruf:
        if x.isupper():
            katbaru = x.lower()
        elif x.islower():
            katbaru = x.upper()
        else:
            katbaru = x
        kata_baru = kata_baru + katbaru
    print("Kalimat baru menjadi :", kata_baru)
    keluar = int(input("Apakah anda ingin keluar ? 1 = Ya 2 = Tidak (1/2) : "))
    if keluar == 1:
        print("Sampai Jumpa")
        break
    elif keluar == 2:
        continue
    else:
        print("Input anda salah")
