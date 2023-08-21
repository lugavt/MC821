'''Done'''

tests = int(input())

for i in range(tests):
    test = input()
    if (test[0] == "y" or test[0] == "Y") and (test[1] == "e" or test[1] == "E") and (test[2] == "s" or test[2] == "S"):
        print("YES")
    else:
        print("NO")