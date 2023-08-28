contadora = 0 
while(1):
    contadora += 1
    aux = input().split()
    itens, friends = int(aux[0]), int(aux[1])
    if(itens == 0 and friends == 0): break
    totalConta = 0
    for i in range(itens):
        totalConta += int(input())
    output = f"Bill #{contadora} costs {totalConta}: each friend should pay {totalConta//friends}"
    print(output)
    