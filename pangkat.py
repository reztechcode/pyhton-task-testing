def hitung_pangkat(x,y):
    hasil = 1
    for i in range(y):
        hasil = hasil * x
    return hasil

def main():
    while True:
        print("Program Menghitung Pangkat")
        x = int(input("Masukkan Banyaknya Angka : "))
        y = int(input("Masukkan Bilangan Bulat  : "))
        
        hasil = hitung_pangkat(x,y)
        print(f"{x} ^ {y} = {hasil}")
        
        tanya_kembali = input("Apakah ingin menghitung pangkat lagi? (ya/tidak): ")
        if tanya_kembali != "ya":
            break

if __name__ == "__main__":
    main()
