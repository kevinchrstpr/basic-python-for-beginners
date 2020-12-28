import os
import math
# Calculator with python by kevinopee

# Fungsi untuk penjumlahan 
def tambah(x, y):
    return x + y

# Fungsi untuk pengurangan 
def kurang(x, y):
    return x - y

# Fungsi untuk perkalian
def kali(x, y):
    return x * y

# Fungsi untuk pembagian
def bagi(x, y):
    return x / y

print("===== Kevin Ope Python Simple Calculator =====\n")
print("Operator yang digunakan : \n")
print("     1. Penjumlahan + \n")
print("     2. Pengurangan - \n")
print("     3. Perkalian x \n")
print("     4. Pembagian / \n")
print("================================================")

while True:
    # Input untuk memilih operator
    operator = input("Pilih operator ( 1 / 2 / 3 / 4 ) : ")

    # Cek fungsi operator yang akan digunakan
    if operator in ('1', '2', '3', '4'):
        no1 = float(input("\nMasukan angka pertama : "))
        no2 = float(input("\nMasukan angka kedua   : "))

        if operator == '1':
            print("\nHasil = ", no1, "+", no2, "=", tambah(no1, no2),"\n")

        elif operator == '2':
            print("\nHasil = ", no1, "-", no2, "=", kurang(no1, no2), "\n")

        elif operator == '3':
            print("\nHasil = ", no1, "*", no2, "=", kali(no1, no2), "\n")

        elif operator == '4':
            print("\nHasil = ", no1, "/", no2, "=", bagi(no1, no2), "\n")
        break
    else:
        print("Input Salah")

os.system("pause")