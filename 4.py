prvi = int(input("unesi poziciju prvog mejsta:"))

drugi = int(input("uensi zaostatak drugog: "))
treci = int(input("uensi zaostatak treceg: "))
cetvrti = int(input("uensi zaostatak cetvrtog: "))
peti = int(input("uensi zaostatak petog: "))
poz1 = int(input("unesi poziciju vozaca koji te zanima (2 - 5): "))
poz2 = int(input("unesi poziciju vozaca koji te zanima (2 - 5): "))

zaostatak = [drugi, treci, cetvrti, peti]


kas = abs(zaostatak[poz1 - 2] - zaostatak[poz2 - 2])


print(f"kasnjenje izmedu vozaca {poz1} i {poz2} je {kas} sekundi.")