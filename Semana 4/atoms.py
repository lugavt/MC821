'''done'''

cases = int(input())

for i in range(cases):
    aux = input().split()
    n, k, m = int(aux[0]), int(aux[1]), int(aux[2])
    t = 0
    while(True):
        n = n*k
        if(n > m): break
        t += 1
    print(t)