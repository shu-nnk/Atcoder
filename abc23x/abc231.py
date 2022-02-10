#A
D=int(input())
MPa=D/100
print(MPa)

#B
N=int(input())
S=[]

for i in range(N):
    s=input()
    S.append(s)

S_set=set(S)
result=""
count=0

for j in S_set:
    temp=S.count(j)
    if temp>=count:
        count=temp
        result=j

print(result)

#C
import bisect
N,Q=map(int,input().split())
A=list(map(int,input().split()))
sorted_A=sorted(A)
for _ in range(Q):
    x=int(input())
    less_index=bisect.bisect_left(sorted_A,x)
    result=N-less_index
    print(result)


