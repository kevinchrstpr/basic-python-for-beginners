# Homework 1, Convert Fahrenheit - > Kelvin and Reverse

print("\n----- PROGRAM KONVERSI SUHU -----\n")

#Celcius -> R = (4/5) * C
#Celcius -> F = (5/9) * C + 32

#Fahrenheit -> Kelvin

c = float(int(input("Masukan Suhu = ")))
Fahrenheit = ( 5 / 9 ) * c - 32
F2 = Fahrenheit + 273
print("Suhu dari Fahrenheit ke Kelvin adalah = ",F2, "Kelvin\n")

c2 = float(int(input("Masukan Suhu = ")))
Kelvin = c2 - 273
K2 = ( 9 / 5 ) * Kelvin + 32
print("Suhu dari Kelvin ke Fahrenheit adalah = ",Kelvin, "Fahrenheit")