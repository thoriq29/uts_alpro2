"""
    author : Thoriqul Azis
    program mencari luas segitiga dengan inputan angka(integer)
"""

def cariLuasSegitiga():
    print("Aplikasi mencari luas segitiga")
    while True:
        try:
            alas = int(input("Silahkan Masukkan Alas Segitiga = "))
            tinggi = int(input("Silahkan Masukkan Tinggi Segitiga = "))
            luas = int(0.5*alas*tinggi)
            print("Luas segitiganya adalah : "+ str(luas))
        except ValueError:
            print("Masukkan Angka saja!")
            continue
        except KeyboardInterrupt:
            print("\nProgram dibatalkan")
            break
        else:
            return luas
            break

cariLuasSegitiga()