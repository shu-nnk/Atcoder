n = int(input())
l = []
for i in range(n):
    b,f,r,v = map(int,input().split())
    l.append([b,f,r,v])

l2 = []
for i in range(4):
    l2.append([
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ])


for i in l:
    l2[i[0] - 1][i[1] - 1][i[2] - 1] +=  i[3]


for i, s in enumerate(l2):
    for j in range(3):
        for k in range(10):
            print(f" {s[j][k]}",end="")
        print()

    if (i!= len(l2)-1):
        print("####################")




