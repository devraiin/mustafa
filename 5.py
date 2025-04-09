unos = input("unsei string: ")
unos = unos.lower()
broj_slova = {}

for karakter in unos:
    if karakter.isalpha():
        if karakter in broj_slova:
            broj_slova[karakter] += 1
        else:
            broj_slova[karakter] = 1

print("broj ponavljanja slova:")
for slovo, broj in sorted(broj_slova.items()):
    print(f"{slovo}: {broj}")