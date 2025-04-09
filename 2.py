broj = input("broj: ")

brojCudnihBrojeva = 0
cudniBrojevi = []

for i in range(len(broj)):
    cifra = int(broj[i])
    poz = i + 1  
    if cifra == poz:
        brojCudnihBrojeva += 1
        cudniBrojevi.append(cifra)

print(f"broj cudnih cifara je: {brojCudnihBrojeva}")
print(" ".join(map(str, cudniBrojevi)))