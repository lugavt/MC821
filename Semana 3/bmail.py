'''done'''

'''input is n of routers and pi's of routers'''

n = int(input())
pi = input().split()
pi = [int(i) for i in pi]
path = [n]
aux = pi[len(pi)-1]
while aux != 1:
    path.append(aux)
    aux = pi[aux-2]

path.append(1)
path.reverse()
for i in path:
    print(i, end=" ")