#Spreadsheet

N, M = list(map(int, input().split())) # 整数
a = []
for i in range(N):
    a.append(list(map(int, input().split())))


for i in range(N):
    add = 0
    for j in range(M):
        add += a[i][j]
    a[i].append(add)

b = []
for j in range(M+1):
    add = 0
    for i in range(N):
        add += a[i][j]
    b.append(add)

a.append(b) 

for i in range(N+1):
    print(' '.join(map(str, a[i])))


