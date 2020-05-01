"""
    author : Thoriqul Azis
    program mencari luas segitiga dengan inputan angka(integer)
"""

def cariLuasSegitiga():
    while True:
        try:
            alas = int(input("Masukkan Alas = "))
            tinggi = int(input("Masukkan Tinggi = "))
            luas = int(0.5*alas*tinggi)
            print("Luas segitiganya adalah : "+ str(luas))
        except ValueError:
            print("Masukkan Angka saja!")
            continue
        else:
            return luas
            break

cariLuasSegitiga()