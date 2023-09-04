cases = int(input())
for i in range(cases):
    days = int(input())
    people = 1
    probability = 1
    while(probability > 0.5):
        probability *= (days-people)/days
        people += 1
    print(f"Case {i+1}:",people-1)