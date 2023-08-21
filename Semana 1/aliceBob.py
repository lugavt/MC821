'''Done'''

testes = int(input())
for i in range(testes):
    numeroAlice = int(input())
    cartasAlice = input().split()
    cartasAlice = [int(numero) for numero in cartasAlice]
    numeroBob = int(input())
    cartasBob = input().split()
    cartasBob = [int(numero) for numero in cartasBob]
    
    maiorCartaAlice = max(cartasAlice)
    maiorCartaBob = max(cartasBob)

    if maiorCartaAlice > maiorCartaBob:
        print("Alice")
        print("Alice")
    elif maiorCartaBob > maiorCartaAlice:
        print("Bob")
        print("Bob")
    else:
        print("Alice")
        print("Bob")
