# Arithmetic Operation
# Remember the basic formula
# () -> ** (Eksponen/Pangkat) -> Multiply -> Divide -> + / - 
a = 10
b = 3

# + 
hasil = a+b
print(a,'+',b,'=',hasil)

# -
hasil = a-b
print(a,'-',b,'=',hasil)

# x
hasil = a*b
print(a,'*',b,'=',hasil)

# :
hasil = a/b
print(a,'/',b,'=',hasil)

# eksponen(pangkat) **
hasil = a**b
print(a,'**',b,'=',hasil)

# modulus(sisa pembagian) %
hasil = a%b
print(a,'%',b,'=',hasil)

# floor division //
hasil = a//b
print(a,'//',b,'=',hasil)

# operational precedence

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x, '**' ,y, '*' ,z, '+' ,x, '/' ,y, '-' ,y, '%' ,z, '//' ,x, '=' ,hasil)

hasil = (x + y) * z
print('(',x, '+' ,y,') *' ,z, '=', hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=', hasil)