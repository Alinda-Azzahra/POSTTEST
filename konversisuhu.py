#Program Konversi Suhu dari Celcius ke Fahrenheit, Kelvin, Reamur.
suhu = int(input("Masukkan suhu celcius: "))

fah = 9/5 * suhu + 32
kev = suhu + 273
rea = 4/5 * suhu

print("C = ", suhu, "C")
print(suhu, "C = ", fah, "F")
print(suhu, "C = ", kev, "K")
print(suhu, "C = ", rea, "R")