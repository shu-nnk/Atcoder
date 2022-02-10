#A
S=input()
a=int(S[0])
b=int(S[2])
print(a*b)

#B
S=input()
T=input()
result="No"

for K in range(26):
    tmp=list(S)
    for i in range(len(S)):
        num=ord(tmp[i])
        change_num=num+K
        if change_num>122:
            change_num=change_num-26
        tmp[i]=chr(change_num)

        if tmp[i]!=T[i]:
            break
    if "".join(tmp)==T:
        result="Yes"
        break

print(result)

#C
import itertools
from unittest import result

N,M=map(int, input().split())
AB=[[False]*N for _ in range(N)]
CD=[[False]*N for _ in range(N)]

for _ in range(M):
    A,B=map(int,input().split())
    AB[A-1][B-1]=True
    AB[B-1][A-1]=True

for _ in range(M):
    C,D=map(int,input().split())
    CD[C-1][D-1]=True
    CD[D-1][C-1]=True

result="No"

for p in itertools.permutations(range(N)):
    judge=True
    for i in range(N):
        for j in range(N):
            if CD[p[i]][p[j]]!=AB[i][j]:
                judge=False
    if judge:
        result="Yes"
        break
print(result)










   

    