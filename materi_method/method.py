class Mahasiswa:
    daftar = 0

    def __init__(self,nama , npm , daftar_hadir , daftar_tidak_hadir):
        
        self.name = nama
        self.npm = npm
        self.daftar_hadir = daftar_hadir
        self.daftar_tidak_hadir = daftar_tidak_hadir
        Mahasiswa.daftar += 1

    # fungsi / method tanpa paramaeter atau void function
    def siapa(self):
        print(f"saya adalah mahasiswa yang bernama {self.name}")

    # fungsi / method dengan parameter
    def recognisi(self, update):
        self.daftar_hadir += update

    # fungsi / method return value
    def list_npm (self):
        return self.npm


# inisialisasi objek dari kelas Mahasiswa
mahasiswa1 = Mahasiswa("achmad" , 20101140078 , 20 , 10)

# pemanggilan method tanpa parameter atau void function 
mahasiswa1.siapa()

# pemanggilan method dengan parameter
mahasiswa1.recognisi(5)
print(f"daftar hadir mahasiswa {mahasiswa1.daftar_hadir}")

# pemanggilan return value
print(mahasiswa1.list_npm())

