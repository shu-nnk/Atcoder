#A
abc=input()
a=abc[0]
b=abc[1]
c=abc[2]

result=int(a+b+c) + int(b+c+a) + int(c+a+b)
print(result) 

#B
N=int(input())
H=list(map(int, input().split()))

i=0

while H[i]<H[i+1]:
    i+=1
    if i==N-1:
        break

print(H[i])

#C
from collections import defaultdict
N,Q=map(int, input().split())
a=list(map(str, input().split()))
#xk=[list(map(str, input().split())) for l in range(N)]
d=defaultdict(list)
for i in range(N):
    d[a[i]].append(i+1)

for j in range(Q):
    x,k = input().split()
    if int(k)<=len(d[x]):
        print(d[x][int(k)-1])
    else:
        print(-1)