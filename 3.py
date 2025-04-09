def prost(broj):
    if broj < 2:
        return False
    for i in range(2, broj):
        if broj % i == 0:
            return False
    return True

N = int(input("N (N < 1000): "))

if N < 1 or N >= 1000:
    print("greska")
else:
    suma = 0
    for broj in range(N, 2 * N + 1):
        if prost(broj):  
            print(broj, end=" ")  
            suma += broj  

    print(f"\nsuma prostih brojeva: {suma}")
