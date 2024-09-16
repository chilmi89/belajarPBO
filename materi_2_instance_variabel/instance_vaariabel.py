class Mobil:
    jumlah_mobil = 0 # instance varibel dari class mobil
    def __init__(self, merk, model, tahun): 
        self.merk = merk
        self.model = model
        self.tahun = tahun
        Mobil.jumlah_mobil += 1
        print(f"merk = {self.merk}\nmodel = {self.model}\ntahun = {self.tahun}")
    def info(self):
        print(self.merk, self.model, self.tahun)

avanza = Mobil("Toyota", "Avanza", 2020)
print(Mobil.jumlah_mobil)
avanza = Mobil("Toyota", "xenia", 2021)
print(Mobil.jumlah_mobil)

