n,m = map(int,input().split())
sum3=0

l=[list(map(int,input().split())) for i in range(n)]

for i in range(n):
    sum=0
    for j in range(m):
        print(f"{l[i][j]}",end=" ")
        sum+=l[i][j]
    print(sum)



for i in range(m):
    sum2=0
    for j in range(n):
        sum2+=l[j][i]
    
    print(sum2,end=" ")
    sum3+=sum2

print(sum3)


