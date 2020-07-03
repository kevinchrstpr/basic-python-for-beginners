# Operasi Komparasi 
# Setiap hasil dari operasi adalah Boolean

# >, <, >=, <=, ==, !=, is, is not

print("\n---------OPERASI KOMPARASI----------\n")

a = 4
b = 2

# lebih besar dari >

hasil = a > b
print('a', '>', 'b', '=', hasil)
hasil = b > a
print('b', '>', 'a', '=', hasil)
hasil = b > b
print('b', '>', 'b', '=', hasil)

print("\n--------------------------------------\n")
# lebih kecil dari <

hasil = b < a
print('b', '<', 'a', '=', hasil)
hasil = a < b
print('a', '<', 'b', '=', hasil)
hasil = a < a
print('a', '<', 'a', '=', hasil)

print("\n--------------------------------------\n")
# lebih besar sama dengan >=

hasil = b >= a
print('b', '>=', 'a', '=', hasil)
hasil = a >= b
print('a', '>=', 'b', '=', hasil)
hasil = a >= a
print('a', '>=', 'a', '=', hasil)

print("\n--------------------------------------\n")
# lebih kecil sama dengan <=

hasil = b <= a
print('b', '<=', 'a', '=', hasil)
hasil = a <= b
print('a', '<=', 'b', '=', hasil)
hasil = a <= a
print('a', '<=', 'a', '=', hasil)

print("\n--------------------------------------\n")
# sama dengan ==

hasil = a == 4 # (a) ada value nya, sedangkan 4 merupakan literal
print('a', '==', '4', '=', hasil)
hasil = a == b
print('a', '==', 'b', '=', hasil)
hasil = a == a
print('a', '==', 'a', '=', hasil)

print("\n--------------------------------------\n")
# tidak sama dengan !=

hasil = a != b
print('a', '!=', 'b', '=', hasil)
hasil = a != b
print('a', '!=', 'b', '=', hasil)
hasil = a != a
print('a', '!=', 'a', '=', hasil)

print("\n--------------------------------------\n")
# 'ís' sebagai komparasi object identity

x = 10 # ini adalah assignment membuat object
y = 10
print('Value of x = ',x,'ID = ', hex(id(x)))
print('Value of Y = ',y,'ID = ', hex(id(y)))
# Jika kedua assignment memiliki nilai yang sama, maka
# Address id yang akan dihasilkan akan sama juga woi wkkw
# Kalo di java, address nya bakal dipisah woi, python lebi mantap

result = x is y
print('x','is','y','=', result)
# Kalo make is, usahain jangan pake literal
# liat nih

result = x is 10 #dimana 10 adalah literal
print('x','is','10','=', result) #liat di terminal,ada syntax warning

print("\n")
# Kalau kedua assignment memiliki nilai yang berbeda, maka
# Yajelas address id nya beda wkakwka
# Liat neh
x = 10
y = 5
print('Value of x = ',x,'ID = ', hex(id(x)))
print('Value of Y = ',y,'ID = ', hex(id(y)))
result = x is y
print('x','is','y','=', result)

print("\n---------------------------------\n")
#'is not' counter clockwise dari is")

x = 10 # ini adalah assignment membuat object
y = 5
print('Value of x = ',x,'ID = ', hex(id(x)))
print('Value of Y = ',y,'ID = ', hex(id(y)))
result = x is not y
print('x','is not','y','=', result)

# See, the id was different but the result is true!

print("\n----------------------------------\n")