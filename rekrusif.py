#------------------------------------------------------
#tujuan : menambahkan fitur kesalahan sistem & fitur tanya kembali pengguna
#         pada program rekursif faktorial dalam bahasa pemograman python
#nama   : Irez Abdullah(2230511041)
#kelas  : TI-3A
#------------------------------------------------------
def factorial(j):
    if j < 0:
        raise ValueError("Faktorial hanya menghitung bilangan bulat yang bernilai positif.")
    if j == 0:
        return 1
    return j * factorial(j - 1)

def get_valid_input():
    try:
        j = int(input("Masukkan bilangan bulat Positif: "))
        if j < 0:
            raise ValueError("bilangan bulat non-positif bukan faktorial.")
        return j
    except ValueError as l:
        print("Error:", l)
        return get_valid_input()

try:
    j = get_valid_input()
    result = factorial(j)
    print(f"{j}! = {result}")
except KeyboardInterrupt:
    print("Proses selesai, pengguna menyelesaikan program.")
except Exception as l:
    print("kesalahan sistem terdeksi:", l)
