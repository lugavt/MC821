# Sum in Binary Tree
'''done'''

cases = int(input())

for i in range(cases):
    vertex = int(input())
    aux = 0
    result = 0
    while(vertex//(2**aux) > 0):
        result += vertex//(2**aux)
        aux += 1
    print(result)