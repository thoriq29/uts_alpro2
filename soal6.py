"""
    author : Thoriqul Azis
    program mencari ganjil genap dengan inputan angka(integer)
"""

# definisikan fungsi untuk mencari angka ganjil genap
def cariGenapGanjil():
  while True:
    try:
        inputan = int(input("Masukkan Angka = "))
        if (inputan % 2 == 0):
            print ("Genap")
        else:
            print ("Ganjil")
    except ValueError:
        print("Masukkan Angka saja!")
        continue
    except KeyboardInterrupt:
        print("\nProgram dibatalkan")
        break
    else:
        return inputan
        break

#panggil fungsi untuk mencari angka ganjil genap
cariGenapGanjil()
