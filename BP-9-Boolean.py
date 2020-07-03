# Logika / Boolean

# not, or, and, xor

print("\n---------- Operasi Logika / Boolean -----------\n")
print('Written by Kevin Christopher')
print('\n---------- NOT ----------\n')
# NOT
a = True
b = not a
print('Data a = ',a)
print('is not')
print('Data c = ',b)

print('\n---------- OR ----------\n')

# OR , jika salah satu dari boolean terdapat true, maka hasil true.
a = True
b = True
c = a or b
print(a ,'OR', b,'  =',c)
a = True
b = False
c = a or b
print(a ,'OR', b,' =',c)
a = False
b = True
c = a or b
print(a ,'OR', b,' =',c)
a = False
b = False
c = a or b
print(a ,'OR', b,'=',c)

print('\n---------- AND ----------\n')

# AND ,jika salah satu boolean terdapat false, maka hasil false.
a = True
b = True
c = a and b
print(a ,'AND', b,'  =',c)
a = True
b = False
c = a and b
print(a ,'AND', b,' =',c)
a = False
b = True
c = a and b
print(a ,'AND', b,' =',c)
a = False
b = False
c = a and b
print(a ,'AND', b,'=',c)

print('\n---------- XOR ----------\n')
#XOR, akan true jika hanya terdapat salah satu true
a = True
b = True
c = a ^ b
print(a ,'XOR', b,'  =',c)
a = True
b = False
c = a ^ b
print(a ,'XOR', b,' =',c)
a = False
b = True
c = a ^ b
print(a ,'XOR', b,' =',c)
a = False
b = False
c = a ^ b
print(a ,'XOR', b,'=',c)