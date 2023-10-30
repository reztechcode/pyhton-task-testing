#------------------------------------------------------
#tujuan : menambahkan fitur kesalahan sistem & fitur tanya kembali pengguna
#         pada program BRUTO FORCE dalam bahasa pemograman python
#nama   : Irez Abdullah(2230511041)
#kelas  : TI-3A
#------------------------------------------------------
import math

def get_valid_input(prompt):
    while True:
        try:
            input_user = int(input(prompt))
            return input_user
        except ValueError:
            print("Masukkan bilangan Bulat :")

def find_gcd(i, j):
    while j:
        i, j = j, i % j
    return i

print("#Program Literasi untuk mencari Faktor Persekutuan Terbesar (FPB) dari dua bilangan.#")

while True:
    try:
        dis1 = get_valid_input("Masukkan Bilangan Pertama: ")
        dis2 = get_valid_input("Masukkan Bilangan Kedua: ")
        
        gcd = find_gcd(dis1, dis2)
        print(f"FPB dari {dis1} dan {dis2} yaitu {gcd}")
        
        another = input("Apakah Anda ingin mencari FPB lagi? (ya/no): ").strip().lower()
        if another != "ya":
            break
    except KeyboardInterrupt:
        print("\n User Memilih No / membatalkan program.")
        break
