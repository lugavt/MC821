cases = int(input())
for i in range(cases):
    digits = int(input())
    red = input()
    blue = input()
    
    newRed = [int(x) for x in red]
    newBlue = [int(x) for x in blue]


    for j in range(len(newRed)):
        if newRed[j] in newBlue:
            newRed.remove(newRed[j])
            newBlue.remove(newBlue[j])

    newRed.sort()
    newBlue.sort()
    redGanha = 0

    for j in range(len(newRed)):
        if(newRed[j] > newBlue[j]):
            redGanha += 1
        elif(newRed[j] < newBlue[j]):
            redGanha -= 1

    if(redGanha > 0): print("RED")
    elif(redGanha < 0): print("BLUE")
    else: print("EQUAL")