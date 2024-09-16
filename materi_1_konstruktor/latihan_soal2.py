# Buatlah kelas Lingkaran yang memiliki atribut jari_jari. 
# Buat konstruktor untuk menginisialisasi jari_jari dan
# tambahkan metode hitung_keliling  dan luas lingkaran.


class Lingkaran:

    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
        self.cetak_info()

    def hitung_keliling(self):
        return 2 * 3.14 * self.jari_jari
    def hitung_luas(self):
        return 3.14 * self.jari_jari**2

    def cetak_info(self):
        print(f"Jari-jari lingkaran = {self.jari_jari}\nkeliling = {self.hitung_keliling()}")
        print("="*20)
        print(f"Jari-jari lingkaran = {self.jari_jari}\nluas = {self.hitung_luas()}")

# Membuat instance dari kelas Lingkaran dengan jari_jari 10 

lingkaran = Lingkaran(10)

