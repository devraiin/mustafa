N = int(input("N: "))
brojCifara = 0
# cifre = []

for i in range(1, N + 1):
    brojCifara += len(str(i))
    # cifre.append(len(str(i)))

print(brojCifara)
# print(cifre)