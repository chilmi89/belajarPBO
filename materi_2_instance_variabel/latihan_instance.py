
# buatlah kelas untuk menyimpan total jumlah pensil
# tammbahkan instance untuk menyimpan warna dan ukuran 

class Pensil:
    jumlah_pensil = 0
    def __init__(self,warna,ukuran):
        self.warna = warna
        self.ukuran = ukuran
       
        Pensil.jumlah_pensil += 1  # memanggil variabel di dalam kelas Pensil
        print(f"warna = {self.warna}\nukuran = {self.ukuran}")



pensil1 = Pensil("merah", 0.5)
print(Pensil.jumlah_pensil)
pensil2 = Pensil("biru", 0.7)
print(Pensil.jumlah_pensil)
pensil3 = Pensil("kuning", 0.3)
print(Pensil.jumlah_pensil)