'''Done'''

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

n = int(input())

for m in range(1, 1001):
    if isPrime(n * m + 1) == False:
        print(m)
        break