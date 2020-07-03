# Data Type Casting
# Changing 1 data type to another data type

#Integer

print("----------- I N T E G E R -----------")
data_int = 9;
print("data = ", data_int, "type = ", type(data_int))

data_float = float(data_int) # Output nya pasti decimal
data_str = str(data_int)
data_bool = bool(data_int)
print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_str, "type = ", type(data_str))
print("data = ", data_bool,"type = ", type(data_bool))

#Float
print("----------- F L O A T -----------")
data_float = 9.5;
print("data = ", data_float, "type = ", type(data_float))

data_int = int(data_float) # Angka diatas 5 pun, pasti diturunin ke bawah
data_str = str(data_float)
data_bool = bool(data_float)
print("data = ", data_int, "type = ", type(data_int))
print("data = ", data_str, "type = ", type(data_str))
print("data = ", data_bool,"type = ", type(data_bool))

#String
print("----------- S T R I N G -----------")
data_str = "9"; # Wajib "Karakter" use ""
print("data = ", data_str, "type = ", type(data_str))

data_int = int(data_str) # Gabakal keluar kalo data stringnya char,wajib angka
data_float = float(data_str) # Sama bae kayak ^
data_bool = bool(data_str) #False kalo string kosong
print("data = ", data_int, "type = ", type(data_int))
print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_bool,"type = ", type(data_bool))


#Boolean , 1 = TRUE
print("----------- B O O L E A N -----------")
data_bool = True; # Gabisa angka/string selain TRUE/FALSE
print("data = ", data_bool, "type = ", type(data_bool))

data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)
print("data = ", data_int, "type = ", type(data_int))
print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_str,"type = ", type(data_str))

#Boolean , 0 = FALSE
print("----------- B O O L E A N 2 -----------")
data_bool = False; # Akan menghasilkan angka 0
print("data = ", data_bool, "type = ", type(data_bool))

data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)
print("data = ", data_int, "type = ", type(data_int))
print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_str,"type = ", type(data_str))