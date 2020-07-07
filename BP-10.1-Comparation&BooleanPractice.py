# Latihan Komparasi dan Operator Boolean / Logika

# Membuat jajaran angka
# rentangnya kurang dari 5 - 10 lebih dari 10

# +++++ 5 ----- 10 +++++
data1 = float(input("Masukan angka < 5 dan > 10 : "))

data2 = (data1 < 5)
print("\nAngka yang dihasilkan : ", data2)

data3 = (data1 > 10)
print("\nAngka yang dihasilkan : ", data3)

data4 = data2 or data3
print("\n Angka yang anda masukan bernilai : ", data4)

# Angka yang dihasilkan akan bernilai false jika < 5 dan > 10
# Sekarang membuat counter clockwise dari project diatas
# Dimana kita akan membuat rentangnya jadi > 5 dan < 10

# ----- 5 +++++ 10 -----
print("\n",10*"-","\n")
data1 = float(input("\nMasukan angka > 5 dan < 10 : "))

data2 = data1 > 5
print("\n Angka yang dihasilkan bernilai : ", data2)

data3 = data1 < 10
print("\n Angka yang dihasilkan bernilai : ", data3)

data4 = data2 and data3
print("\n Angka yang dimasukan bernilai : ", data4)

# Dimana syntax and mendefinisikan kedua data tersebut true or false
# Di rentang yang sudah ditentukan :D

# Oke jadi sekarang kita bakal membuat multi project and or
# Rentang nya dari ----- 0 +++++ 5 ----- 8 +++++ 11 -----
# Berarti < 0, > 5, < 8, dan > 11