#------------------------------------------------------
#tujuan : menambahkan fitur kesalahan sistem & fitur tanya kembali pengguna
#         pada program BRUTO FORCE dalam bahasa pemograman python
#nama   : Irez Abdullah(2230511041)
#kelas  : TI-3A
#------------------------------------------------------
import random

# Menebak angka acak antara 20 dan 53
target_number = random.randint(20, 50)

while True:
    try:
        guess = int(input("Masukkan tebakan angka dari 20 sampai 53: "))
    except ValueError:
        print("Angka tidak valid.")
        continue

    if guess < 20 or guess > 50:
        print("Angka harus dari 20 sampai 53.")
        continue

    if guess < target_number:
        print("Angka terlalu kecil.")
    elif guess > target_number:
        print("Angka terlalu besar.")
    else:
        print("Tebakan benar.")
        break
