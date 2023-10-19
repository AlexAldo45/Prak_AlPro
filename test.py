class Makanan:
    def __init__(self, nama, kalori):
        self.nama = nama
        self.kalori = kalori
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, nama, kalori):
        new_makanan = Makanan(nama, kalori)
        if self.is_empty():
            self.top = new_makanan
        else:
            new_makanan.next = self.top
            self.top = new_makanan

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print(f"Data {self.top.nama} ({self.top.kalori} kal) discarded!")
            self.top = self.top.next

    def print_history(self):
        if self.is_empty():
            print("No data available.")
        else:
            current = self.top
            while current:
                print(f"Data {current.nama} ({current.kalori} kal)")
                current = current.next


stack = Stack()

jenis_kelamin = int(input("Pilih Jenis Kelamin:\n1. Pria\n2. Wanita\nPilihan Anda : "))

if jenis_kelamin == 1:
    batas_kalori = 2000
else:
    batas_kalori = 1500

total_kalori = 0

while True:
    print(f"\nPilih Menu:\n1. Makan\n2. Buang\n3. Riwayat Makanan\n4. Keluar\nKalori saat ini: {total_kalori} kal")
    menu = int(input("Pilihan Anda : "))

    if menu == 1:
        nama = input("Masukkan nama : ")
        kalori = int(input("Masukkan kalori : "))

        if total_kalori + kalori <= batas_kalori:
            stack.push(nama, kalori)
            total_kalori += kalori
            print(f"Data {nama} ({kalori} kal) disimpan!")
        else:
            print("Penambahan makanan dibatalkan, total kalori melebihi batas!")
    elif menu == 2:
        count = 0
        current = stack.top
        while current:
            current = current.next
            count += 1
        to_be_removed = count // 2
        for _ in range(to_be_removed):
            stack.pop()
            total_kalori -= stack.top.kalori
    elif menu == 3:
        print("Riwayat Makanan:")
        stack.print_history()
    elif menu == 4:
        break
