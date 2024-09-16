
# Membuat Kelas dengan Konstruktor
# 1. Buatlah kelas Mobil yang memiliki atribut merk, model, dan tahun.
# 2. Buat konstruktor untuk menginisialisasi atribut-atribut tersebut.
# 3. Tambahkan metode untuk menampilkan informasi mobil.


class Mobil:
    # Konstruktor kelas Mobil yang menerima tiga parameter: merk, model, dan tahun
    def __init__(self, merk, model, tahun): 
        self.merk = merk
        self.model = model
        self.tahun = tahun
    # fungsi info untuk menampilkan informasi mobil
    def info(self):
        print(self.merk, self.model, self.tahun)

# Membuat instance dari kelas mobil
avanza = Mobil("Toyota", "Avanza", 2020)
# Mencetak informasi mobil
set_info = avanza.info()
