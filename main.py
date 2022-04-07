import random

x = 10
y = 10

N = 20
tabel = {'node':{},'neighbor':{}}
for i in range(N):
    tabel['node'][i] = {}
    tabel['node'][i]['x'] = random.randint(0, 9)
    tabel['node'][i]['y'] = random.randint(0, 9)
# for i in range(len(tabel['node'])):

print(tabel)

for i in range(x):
    for j in range(y):
        found = False
        for t in range(len(tabel['node'])):
            if tabel['node'][t]['x'] == i and tabel['node'][t]['y'] == j:
                found = True
                break
        if found:
            print(" x ", end="")
        else:
            print(" . ", end="")
    print()
    