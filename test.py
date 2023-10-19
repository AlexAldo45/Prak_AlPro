
import java.util.Scanner;

class Makanan {
    String nama;
    int kalori;
    Makanan next;

    public Makanan(String nama, int kalori) {
        this.nama = nama;
        this.kalori = kalori;
        this.next = null;
    }
}

class Stack {
    Makanan top;

    public Stack() {
        this.top = null;
    }

    public boolean isEmpty() {
        return top == null;
    }

    public void push(String nama, int kalori) {
        Makanan newMakanan = new Makanan(nama, kalori);
        if (isEmpty()) {
            top = newMakanan;
        } else {
            newMakanan.next = top;
            top = newMakanan;
        }
    }

    public void pop() {
        if (isEmpty()) {
            System.out.println("Stack is empty!");
        } else {
            System.out.println("Data " + top.nama + " (" + top.kalori + " kal) discarded!");
            top = top.next;
        }
    }

    public void printHistory() {
        if (isEmpty()) {
            System.out.println("No data available.");
        } else {
            Makanan current = top;
            while (current != null) {
                System.out.println("Data " + current.nama + " (" + current.kalori + " kal)");
                current = current.next;
            }
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Stack stack = new Stack();

        int jenisKelamin;
        int batasKalori;
        int totalKalori = 0;

        System.out.println("Pilih Jenis Kelamin:\n1. Pria\n2. Wanita");
        System.out.print("Pilihan Anda : ");
        jenisKelamin = scanner.nextInt();

        if (jenisKelamin == 1) {
            batasKalori = 2000;
        } else {
            batasKalori = 1500;
        }

        while (true) {
            System.out.println("\nPilih Menu:\n1. Makan\n2. Buang\n3. Riwayat Makanan\n4. Keluar\nKalori saat ini: " + totalKalori + " kal");
            System.out.print("Pilihan Anda : ");
            int menu = scanner.nextInt();

            if (menu == 1) {
                System.out.print("Masukkan nama : ");
                String nama = scanner.next();
                System.out.print("Masukkan kalori : ");
                int kalori = scanner.nextInt();

                if (totalKalori + kalori <= batasKalori) {
                    stack.push(nama, kalori);
                    totalKalori += kalori;
                    System.out.println("Data " + nama + " (" + kalori + " kal) disimpan!");
                } else {
                    System.out.println("Penambahan makanan dibatalkan, total kalori melebihi batas!");
                }
            } else if (menu == 2) {
                int count = 0;
                Makanan current = stack.top;
                while (current != null) {
                    current = current.next;
                    count++;
                }
                int toBeRemoved = count / 2;
                for (int i = 0; i < toBeRemoved; i++) {
                    stack.pop();
                    totalKalori -= stack.top.kalori;
                }
            } else if (menu == 3) {
                System.out.println("Riwayat Makanan:");
                stack.printHistory();
            } else if (menu == 4) {
                break;
            }
        }
    }
}
