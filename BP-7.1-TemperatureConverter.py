# Latihan Konversi Suhu ^^

# Program Konversi Celcius -> Kelvin -> Fahrenheit -> Reamur

print("\n----- PROGRAM KONVERSI SUHU -----\n")

celcius = float(input('Input suhu dalam celcius = '))
print("Suhu akhir = ", celcius, "Celcius")

#Reamur
Reamur = ( 4 / 5 ) * celcius
print("Suhu dalam Reamur = ", Reamur, "Reamur")

#Fahrenheit
Fahrenheit = ( 9 / 5 ) * celcius + 32
print("Suhu dalam Fahrenheit = ", Fahrenheit, "Fahrenheit")

#Kelvin
Kelvin = celcius + 273
print("Suhu dalam Kelvin = ", Kelvin, "Kelvin")