print("TABEL KEBENARAN KONJUNGSI")
print("-------------------------")

print("n\|P\t|Q\t|P AND Q|")
print("-------------------------")

for P in [True,False]:
    for Q in [True,False]:
        Konjungsi = P and Q
        print(f"{P}\t{Q}\t{Konjungsi}")

print("\n|P\t|Q\t|P OR Q")
print("-------------------------")
print("TABEL KEBENARAN DISJUNGSI")
print("-------------------------")

for P in [True,False]:
    for Q in [True,False]:
        Disjungsi = P or Q
        print(f"{P}\t{Q}\t{Disjungsi}")
        
print("\n|P\t|Q\t|P NOT Q")
print("-------------------------")
print("TABEL KEBENARAN NEGASI")
print("----------------------") 

for P in [True,False]:
    for Q in [True,False]:
        Negasi = not P
        print(f"{P}\t{Q}\t{Negasi}")

print("\n|P\t|Q\t|-P OR Q")
print("-------------------------")
print("TABEL KEBENARAN NEGASI")
print("----------------------")

for P in [True,False]:
    for Q in [True,False]:
        Negasi = not P or Q
        print(f"{P}\t{Q}\t{Negasi}")  
