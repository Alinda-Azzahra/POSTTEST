#Inputan data dengan tema benda (buku)
buku = []
#Variabel 1
buku1 = input("Masukkan judul buku : ")
print("Judul : ", buku1, "Tipe data : ", type(buku1), end="\n\n")
buku.append(buku1)

#Variabel 2
buku2 = int(input("Masukkan jumlah halaman : "))
print("Jumlah halaman : ", buku2, "halaman,", "Tipe data : ", type(buku2), end="\n\n")
buku.append(buku2)

#Variabel 3
buku3 = float(input("Masukkan berat buku : "))
print("Berat buku : ", buku3, "gram,", "Tipe data : ", type(buku3), end="\n\n")
buku.append(buku3)

#Variabel 4
buku4 = input("Masukkan penulis buku : ")
print("Nama penulis : ", buku4, "Tipe data : ", type(buku4), end="\n\n")
buku.append(buku4)

#Variabel 5
buku5 = int(input("Masukkan harga buku : "))
print("Harga buku : ", buku5, "Tipe data : ", type(buku5), end="\n\n")
buku.append(buku5)

#List
print (buku[0:6])
