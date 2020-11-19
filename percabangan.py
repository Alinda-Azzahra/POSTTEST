#Program Percabangan

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("*" * 50)
print("\t\t  SELAMAT DATANG\n")
print("\t\tTAKOYAKI ENAK LOH")
print("*" * 50)
beli = str(input("Apakah anda ingin membeli takoyaki?"))

def varian():
    clear_screen()
    print("~" * 30)
    print("\t Silahkan Pilih")
    print("~" * 30)
    print("1. Varian 1: Rp 2000/pcs")
    print("2. Varian 2: Rp 2500/pcs")
    print("3. Tidak jadi")
    pilih = input("Pilih Varian>>> ")
    
    if(pilih == "1"):
        varian_satu()
    elif(pilih == "2"):
        varian_dua()
    elif(pilih == "3"):
        clear_screen()
        print("*" * 41)
        print("Terimakasih, silahkan datang kembali ^_^")
        print("*" * 41)
        exit()
    else:
        print("Varian yang kamu pilih tidak ada")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter Untuk Kembali...")
    varian()

def varian_satu():
    clear_screen()
    print("~" * 28)
    print("\t  Varian 1")
    print("~" * 28)

    jumlah = int(input("Jumlah pesanan: "))
    bayar = int(jumlah) * 2000

    if int(jumlah) >= 10:
        print("Selamat karena anda membeli takoyaki >= 10 pcs, anda mendapatkan diskon 10%!!!")
        diskon = int(jumlah) * 2000 * 10/100
        bayar = diskon
    
    print("Total yang harus dibayar: Rp %s" %bayar)
    print("Terimakasih, Silahkan datang kembali ^_^")
    exit()

def varian_dua():
    clear_screen()
    print("~" * 28)
    print("\t  Varian 2")
    print("~" * 28)
    
    jumlah = int(input("Jumlah pesanan: "))
    bayar = jumlah * 2500

    if int(jumlah) >= 8:
        print("Selamat karena anda membeli takoyaki >= 8 pcs, anda mendapatkan diskon 8%!!!")
        diskon = int(jumlah) * 2500 * 8/100 
        bayar = diskon

    print("Total yang harus dibayar: Rp %s" %bayar)
    print("Terimakasih, Silahkan datang kembali ^_^")
    exit()

if __name__ == "__main__":
    while True:
        varian()