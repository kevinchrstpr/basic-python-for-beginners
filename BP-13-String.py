# 1. How to make string, bitches
# String adalah kumpulan karakter (char)

data = "THIS WUZ STRING BITCHES"
print(data)
print(type(data))

'''
    1. Pake single quote ''
    2. Pake double quote ""
'''

data = 'INI SINGLE QUOTE'
print(data)

data = "INI DOUBLE QUOTE"
print(data)

print("'INI SINGLE QOUTE DALAM DOUBLE QOUTE'")
print('"INI DOUBLE QUOTE DALAM SINGLE QUOTE"')
print(" HARI INI ADALAH HARI JUM'AT") 
# Karena hari jum'at memakai kutip satu, maka harus memakai double quote
# agar single quote di hari jumat tsb dianggap string

# 2. Menggunakan \ sebagai penganggap symbol sbg string
print('Today was so fun, wasn\'t it?')

# Backslash

#Print percis kayak di bawah tapi backlash nya satu aja (\)
#PYTHONNYA BAKAL BINGUNG CEK TERMINAL KWKWKW
# TAPI KALO BACKSLASH NYA DUA
print("C:\\Users\\kevin\\Documents\\00 - Template 1")
# IT WORKED

# Tab
print("kevin ganteng") # FAKTA Y
print("kevin gan\teng, teng nya minggat wkwkwk")
# \t bisa kalian pake kalo mau bikin teks biar ditengah lah, apalah
# tanpa harus menggunakan spasi satu satu
# kan pegel wkoakwaokawowka

# Backspace (delete spasi coeg sepelee deh pokoknya)
print("Kevin \bego, nah ini karna ga fakta, jadi ego wkwk")
# gunanya ya backspace, sama kayak di keyboard

# Newline , enter biasa aja ini, selow gausah ngegas
print("Baris pertama \nbaris kedua") # lf -> line feed
print("Baris pertama \rbaris kedua") # cr -> carriage return
print("Baris pertama \r\nbaris kedua") # crlf -> line feed carriage return

# 3. Literal String atau Raw
# bukan raw smackdown ye

print("C:\newRAW") # path nya salah, karena dikira bikin newline wkkw
# kalo begini
print(r"C:\newRaw") # lokit terminal coba, alus dah wkwk
# nih misalkan random yak pake banyak lfcr kek apakek
print(r"C:\newRaw\tokai\lacot")

# multiline literal string
print("""
Name : Kevin Ganteng
Univ : Universitas Pembangunan Jaya
""")

# multiline literal string & raw
print(r"""
Nama : Kevin ganzzz bett \n
Univ : Univ Pembangunan Jaya
Web  : github.com/kevinchrstpr/basic-python-for-beginner
""")