package com.ug3.soal1;
import java.util.*;
import java.util.Scanner;
public class UG3Soal1 {
    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        System.out.println("============absensi karyawan============");
        System.out.print("Nama Karyawan : ");
        String nama = inp.nextLine();


        System.out.println("berhasil absensi");
        System.out.println("Atas nama : "+nama);
        GregorianCalendar tanggal = new GregorianCalendar();

        String namabulan[] = {"Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"};

        int hari = tanggal.get(Calendar.DAY_OF_MONTH);
        int bulan = tanggal.get(Calendar.MONTH);
        int tahun = tanggal.get(Calendar.YEAR);
        int detik = tanggal.get(Calendar.SECOND);
        int menit = tanggal.get(Calendar.MINUTE);
        int jam =  tanggal.get(Calendar.HOUR_OF_DAY);
        System.out.println("Pada tanggal : "+hari+"-"+namabulan[bulan]+"-"+tahun);
        System.out.println("Pukul : "+jam+":"+menit+":"+detik);
    }
}
