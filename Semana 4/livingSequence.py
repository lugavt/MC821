cases = int(input())

for i in range(cases):
    case = input()
    aux = int(case)
    for j in range(len(case)):
        aux += int(case[j])*9**(len(case)-j-1)
        
        print(aux)