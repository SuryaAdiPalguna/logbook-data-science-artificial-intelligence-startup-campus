import os, daily_logbook, weekly_logbook, monthly_logbook, final_report

def main():
  pilihan = -1
  while pilihan != 0:
    os.system("cls")
    print("APLIKASI REGENERATE LOGBOOK")
    print()
    print("Pilihan Menu:")
    print("1. Daily Logbook")
    print("2. Weekly Logbook")
    print("3. Monthly Logbook")
    print("4. Final Report")
    print("0. Keluar")
    pilihan = int(input("Masukkan Pilihan: "))

    if pilihan == 1:
      os.system("cls")
      daily_logbook.main()
      os.system("PAUSE")
    elif pilihan == 2:
      os.system("cls")
      weekly_logbook.main()
      os.system("PAUSE")
    elif pilihan == 3:
      os.system("cls")
      monthly_logbook.main()
      os.system("PAUSE")
    elif pilihan == 4:
      os.system("cls")
      final_report.main()
      os.system("PAUSE")
    elif pilihan == 0:
      print()
      print("Terima Kasih")
    else:
      print()
      print("Pilihan Tidak Tersedia")
      os.system("PAUSE")

if __name__ == "__main__":
  main()