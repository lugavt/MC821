def fatorial(n):
    if n == 0 or n == 1: return 1
    return n * fatorial(n - 1)

n = int(input())
print(int(((fatorial(n)/fatorial(n/2)**2)//2)*fatorial(n/2 - 1)**2))