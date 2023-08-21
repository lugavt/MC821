'''done'''

'''inputs are a,b,c,d for probabilities'''

arr = input().split()
a,b,c,d = int(arr[0]),int(arr[1]),int(arr[2]),int(arr[3])
probSmallArcher = a/b
probZanoes = c/d

result = probSmallArcher/(1-(1-probSmallArcher)*(1-probZanoes))

print(result)