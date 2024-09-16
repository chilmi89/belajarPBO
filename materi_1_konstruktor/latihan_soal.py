# menggunakan Konstruktor untuk Menghitung Luas Persegi Panjang
# Buatlah kelas PersegiPanjang dengan atribut panjang dan lebar.
# Buat konstruktor untuk menginisialisasi atribut-atribut tersebut dan
# tambahkan metode hitung_luas untuk menghitung luas persegi panjang.



class Rumus:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
        self.cetak_info()
        

    def hitung_luas(self):
        return self.lebar * self.panjang
    
    def cetak_info(self):
        print(f"panjang persegi = {self.panjang}\nlebar persegi = {self.lebar}\nluas = {self.hitung_luas()}")

# Membuat instance dari kelas PersegiPanjang dengan panjang 10 dan lebar 5

persegi_panjang = Rumus(10, 5)

# Mencetak luas persegi panjang

# Mencetak luas persegi panjang     
