'''done'''

cases = int(input())

for i in range(cases):
    template = input()
    matches = 1
    for j in range(len(template)):
        if(template[j] == '?'):
            if j == 0: matches *= 9
            else: matches *= 10

    if(template.count('0') == len(template) or template[0] == '0'): matches = 0
    print(matches)