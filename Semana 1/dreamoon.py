'''done'''

correctString = input()
correctResult = 0

for i in correctString:
    if(i == '-'): correctResult -= 1
    else: correctResult += 1

receivedString = input()
receivedResult = 0
doubts = 0

for i in receivedString:
    if(i == '-'): receivedResult -= 1
    elif(i == '+'): receivedResult += 1
    else: doubts += 1

if(doubts == 0):
    if((correctResult == receivedResult)): print(1)
    else: print(0)

else:
    if(abs(correctResult - receivedResult) > doubts): print(0)
    else:
        arrPossibilities = []
        '''calculate all possibilities of + and -'''
        for i in range(2**doubts):
            arrPossibilities.append(bin(i)[2:].zfill(doubts))
        
        rightCases = 0
        for i in arrPossibilities:
            result = receivedResult
            for j in i:
                if(j == '0'): result -= 1
                else: result += 1
            if(result == correctResult):
                rightCases += 1
        print(rightCases/len(arrPossibilities))


