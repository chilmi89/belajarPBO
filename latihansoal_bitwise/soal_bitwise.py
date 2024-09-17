from prettytable import PrettyTable
a = 10
b = 12

hasil_and = a & b
hasil_or = a | b
hasil_xor = a ^ b

print(f"nilai dari a = {a} dan nilai binernya =  {bin(a)}\nbilai dari b = {b} dan nilai binarnya = {bin(b)}") 
print(f"hasil AND dari a dan b dalam desimal = {hasil_and}")
print(f"hasil OR dari a dan b dalam desimal  = {hasil_or}")
print(f"hasil XOR dari a dan b dalam desimal = {hasil_xor}")

tabel_kebenaran = PrettyTable()
tabel_kebenaran.field_names = ["a", "b", "a AND b", "a OR b", "a XOR b"]

for i in range(2):
    for j in range(4):
        a = i
        b = j
        tabel_kebenaran.add_row([a, b, a & b, a | b, a ^ b])

print(tabel_kebenaran)
