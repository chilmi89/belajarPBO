# Mendefinisikan sebuah kelas bernama Subjek
class Subjek:
    # Konstruktor kelas Subjek yang menerima tiga parameter: nama, umur, dan hobi
    def __init__(self, nama, umur, hobi):
        # Menginisialisasi atribut nama dengan nilai parameter nama
        self.nama = nama
        # Menginisialisasi atribut umur dengan nilai parameter umur
        self.umur = umur
        # Menginisialisasi atribut hobi dengan nilai parameter hobi
        self.hobi = hobi

# Membuat instance dari kelas Subjek dengan nama "chilmi", umur 20, dan hobi "mancing"
Subjek1 = Subjek("chilmi", 20, "mancing")
# Mencetak nilai atribut nama, umur, dan hobi dari instance Subjek1
print(Subjek1.nama , Subjek1.umur, Subjek1.hobi)
