#Nama: Alexander Aldo Siandica Nugroho
#Univertas Kristen Duta Wacana

'''
Andi mempunyai ayah yang bekerja di bagian pembayaran di bis, setiap hari ayah andi melayani orang dengan 
menghitung manual seperti melihat jauh orang itu melakukan perjalanan, menghitung total pembayaran, dan kembalian uang. 
Bantulah ayah Andi untuk membuatkannya program yang dapat menentukan jarak perjalanan orang yang ingin ditempuh, total harganya,
dan kembalian uang.

catatan: 
1-10 km = 7.000
11-15 km = 15.000
16-25 km = 25.000
26-35 km = 40.000
35 km lebih = 40.000 + harga ditambah 5.000/km
'''
'''
Input: user memasukkan jarak perjalanan, uang yang dibawa orang itu, dan keluar dar program
Proses: menentukan jarak perjalanan lalu menghitung jumlah harganya, dan kembaliannya
Output: total pembayaran, uang kembalian jarak yang ingin ditempuh
'''

while True:
    loop = True
    user = input("Masukkan jarak perjalanan yang ingin ditempuh (Km) : ")
    bayar = input("Masukkan uang pembayaran anda : ")
    
    try:
        pilih = int(user)
        uang = int(bayar)


        if pilih >=1 and pilih <= 10:
            harga_1 = 7000
            print("Anda akan menempuh perjalanan sejauh : ", pilih, "Km")
            print("Total pembayaran yaitu : Rp.", harga_1)
            kembali_1 = uang - harga_1
            if kembali_1 < 0 :
                print("Maaf uang anda tidak mencukupi")
            elif kembali_1 >= 0 :
                print("Uang kembalian anda adalah : Rp.", kembali_1)
                keluar = str.lower(input("Apakah anda ingin keluar ? ketik (Y/N) : "))
                if keluar == "y":
                    break
                elif keluar == "n":
                    continue
                else:
                    print("Maaf input yang anda masukkan salah")
                    loop = False
        elif pilih >= 11 and pilih <= 15:
            harga_2 = 15000
            print("Anda akan menempuh perjalanan sejauh : ", pilih, "Km")
            print("Total pembayaran yaitu : Rp.", harga_2)
            kembali_2 = uang - harga_2
            if kembali_2 < 0 :
                print("Maaf uang anda tidak mencukupi")
            elif kembali_2 >= 0 :
                print("Uang kembalian anda adalah : Rp.", kembali_2)
                keluar = str.lower(input("Apakah anda ingin keluar ? ketik (Y/N) : "))
                if keluar == "y":
                    break
                elif keluar == "n":
                    continue
                else:
                    print("Maaf input yang anda masukkan salah")
                    loop = False
        elif pilih >= 16 and pilih <= 25:
            harga_3 = 25000
            print("Anda akan menempuh perjalanan sejauh : ", pilih, "Km")
            print("Total pembayaran yaitu : Rp.", harga_3)
            kembali_3 = uang - harga_3
            if kembali_3 < 0 :
                print("Maaf uang anda tidak mencukupi")
            elif kembali_3 >= 0 :
                print("Uang kembalian anda adalah : Rp.", kembali_3)
                keluar = str.lower(input("Apakah anda ingin keluar ? ketik (Y/N) : "))
                if keluar == "y":
                    break
                elif keluar == "n":
                    continue
                else:
                    print("Maaf input yang anda masukkan salah")
                    loop = False
                    
        elif pilih >= 26 and pilih <= 35:
            harga_4 = 40000
            print("Anda akan menempuh perjalanan sejauh : ", pilih, "Km")
            print("Total pembayaran yaitu : Rp.", harga_4)
            kembali_4 = uang - harga_4
            if kembali_4 < 0 :
                print("Maaf uang anda tidak mencukupi")
            elif kembali_4 >= 0 :
                print("Uang kembalian anda adalah : Rp.", kembali_4)
                keluar = str.lower(input("Apakah anda ingin keluar ? ketik (Y/N) : "))
                if keluar == "y":
                    break
                elif keluar == "n":
                    continue
                else:
                    print("Maaf input yang anda masukkan salah")
                    loop = False
        elif pilih > 35:
            harga_5 = pilih - 35
            harga_6 = (harga_5 * 5000) + 40000
            print("Anda akan menempuh perjalanan sejauh : ", pilih, "Km")
            print("Total pembayaran yaitu : Rp.", harga_6)
            kembali_5 = uang - harga_6
            if kembali_5 < 0 :
                print("Maaf uang anda tidak mencukupi")
            elif kembali_5 >= 0 :
                print("Uang kembalian anda adalah : Rp.", kembali_5)
                keluar = str.lower(input("Apakah anda ingin keluar ? ketik (Y/N) : "))
                if keluar == "y":
                    break
                elif keluar == "n":
                    continue
                else:
                    print("Maaf input yang anda masukkan salah")
                    loop = False

    except:
        print("Maaf input yang anda masukkan salah")
        loop = False

