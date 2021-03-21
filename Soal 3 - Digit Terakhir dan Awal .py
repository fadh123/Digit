'''
Buatlah sebuah file python yang berisi 2 buah return function, dengan 2 argumen (a dan b) yang dapat
digunakan untuk menentukan digit awal dan digit akhir dari sebuah operasi matematika a
b. Jika hasil pangkat
hanya satu digit maka digit awal dan akhirnya adalah sama.
'''
'''
-fungsi digitAwal(...) akan memberikan digit awal dari hasil operasi matematika a
b. Contoh output yang
diharapkan adalah sebagai berikut:
# Function Initialization :
def digitAwal(...):
 ......
def digitAkhir(...):
 ......
 
 
# Use the function
print(digitAwal(10,8))
print(digitAwal(2,3))
print(digitAwal(6,3))
# Output:
1
8
2
-Sedangkan fungsi digitAkhir(...) akan memberikan digit akhir dari operasi matematika a
b. Contoh
output yang diharapkan adalah sebagai berikut:
# Use the function
print(digitAkhir(10,8))
print(digitAkhir(2,3))
print(digitAkhir(6,3))
# Output:
0
8
6
'''

# Memasukkan Function Digit Awal dan Digit Akhir

#Digit Awal
def digitAwal(x, n):
    if n == 1:
        return x
    else:
        return x * digitAwal (x, n -1)
print('10^8 =', digitAwal(10,8))
print('2^3 =', digitAwal(2,3))
print('6^3 =', digitAwal(6,3))

digitAwal1 = "100000000"
print(digitAwal1[0])
digitAwal2 = "8"
print(digitAwal2[0])
digitAwal3 = "216"
print(digitAwal3[0])

#Digit Akhir
def digitAkhir(a, b):
    if b == 1:
        return a
    else:
        return a * digitAkhir (a, b -1)
print('10^8 =', digitAkhir(10,8))
print('2^3 =', digitAkhir(2,3))
print('6^3 =', digitAkhir(6,3))

digitAkhir1 = "100000000"
print(digitAkhir1[-1])
digitAkhir2 = "8"
print(digitAkhir2[-1])
digitAkhir3 = "216"
print(digitAkhir3[-1])
