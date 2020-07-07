# Bitwise / Binary
# OR, AND, NOT, XOR

a = 9
b = 5

# OR (|)
c = a | b
print('===== OR =====\n')
print('nilai : ',a,', binary : ', format(a,'08b'))
print('\nnilai : ',b,', binary : ', format(b,'08b'))
print("-------------------------------------")
print('nilai : ',c,', binary : ', format(c,'08b'))

# AND (&)
c = a & b
print('\n===== AND =====')
print('\nnilai : ',a,' binary : ', format(a,'08b'))
print('\nnilai : ',b,' binary : ', format(b,'08b'))
print("-------------------------------------")
print('nilai : ',c,' binary : ', format(c,'08b'))

# XOR (^)
c = a ^ b
print('\n===== XOR =====')
print('\nnilai : ',a,' binary : ', format(a,'08b'))
print('\nnilai : ',b,' binary : ', format(b,'08b'))
print("-------------------------------------")
print('nilai : ',c,' binary : ', format(c,'08b'))

# NOT (~)
c = ~a
print('\n===== AND =====')
print('\nnilai : ',a,' binary : ', format(a,'08b'))
print("-------------------------------------")
print('nilai : ',c,' binary : ', format(c,'08b'))

# Shifting Right (>>)
c = a >> 1
print('\n===== >> =====')
print('\nnilai : ',a,', binary : ',format(a,'08b'))
print("-------------------------------------")
print('\nnilai : ',c,', binary : ',format(c,'08b'))

# Shifting Left (<<)
c = a << 1
print('\n===== << =====')
print('\nnilai : ',a,', binary : ',format(a,'08b'))
print("-------------------------------------")
print('\nnilai : ',c,', binary : ',format(c,'08b'))