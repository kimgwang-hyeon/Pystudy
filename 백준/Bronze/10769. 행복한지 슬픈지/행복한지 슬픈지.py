arr = input().split()
happy = 0
sad = 0
for i in arr:
    if len(i) < 3:
        continue
    for j in range(len(i) - 2):
        if i[j] + i[j+1] + i[j + 2] == ':-)':
            happy += 1
        elif i[j] + i[j+1] + i[j + 2] == ':-(':
            sad += 1
if happy > sad:
    print('happy')
elif happy != 0 and happy == sad:
    print('unsure')
elif happy < sad:
    print('sad')
elif happy == sad == 0:
    print('none')