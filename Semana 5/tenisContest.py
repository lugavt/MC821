def fatorial(n):
    if n == 0 or n == 1: return 1
    return n * fatorial(n - 1)

def combination(n, r):
    return int(fatorial(n)/(fatorial(r)*fatorial(n - r)))

cases = int(input())
for i in range(cases):
    gamesToWin = int(input())
    probabilityPerGame = float(input())

    chance = 0
    for i in range(gamesToWin):
        chance += probabilityPerGame**gamesToWin * (combination(gamesToWin+i-1,i)*(1-probabilityPerGame)**i)

    print(f"{chance:.2f}")