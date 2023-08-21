tests = int(input())
for i in range(tests):
    aux = input().split()
    size, maxDiff = int(aux[0]), int(aux[1])
    sequence = input().split()
    sequence = [int(number) for number in sequence]
    