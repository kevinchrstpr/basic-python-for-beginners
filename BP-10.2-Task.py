# Oke jadi sekarang kita bakal membuat multi project and or
# Rentang nya dari ----- 0 +++++ 5 ----- 8 +++++ 11 -----
# Berarti < 0, > 5, < 8, dan > 11
# And Also the counter clockwise from the task above >_<

# Task 1
print(5*"-","Task 1", 5*"-", "\n")
data1 = float(input("Masukan Angka : "))

moredata2 = data1 > 0
print("\nAngka yang dimasukan bernilai : ", moredata2)

lessdata3 = data1 < 5 
print("\nAngka yang dimasukan bernilai : ", lessdata3)

moredata4 = data1 > 8
print("\nAngka yang dimasukan bernilai : ", moredata4)

lessdata5 = data1 < 11
print("\nAngka yang dimasukan bernilai : ", lessdata5)

# ----- 0 +++++ 5 ----- 8 +++++ 11

data6 = moredata2 or lessdata3
print("\nTotal angka yang dimasukan bernilai : ", data6)
#cause we dont use if, so we split the syntax
data7 = moredata4 and lessdata5
print("\nTotal angka yang dimasukan bernilai : ", data7)

# Task 2
print("\n",5*"-","Task 2", 5*"-")
data1 = float(input("\nMasukan Angka : "))

moredata2 = data1 < 0
print("\nAngka yang dimasukan bernilai : ", moredata2)

lessdata3 = data1 > 5 
print("\nAngka yang dimasukan bernilai : ", lessdata3)

moredata4 = data1 < 8
print("\nAngka yang dimasukan bernilai : ", moredata4)

lessdata5 = data1 > 11
print("\nAngka yang dimasukan bernilai : ", lessdata5)

# +++++ 0 ----- 5 +++++ 8 ----- 11

data6 = moredata2 and lessdata3
print("\nTotal angka yang dimasukan bernilai : ", data6)
#cause we dont use if, so we split the syntax
data7 = moredata4 or lessdata5
print("\nTotal angka yang dimasukan bernilai : ", data7)
