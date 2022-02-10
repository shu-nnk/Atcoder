#B
"""
S,T = map(int,input().split())
count=0

for a in range(100):
    for b in range(100):
        for c in range(100):
            if (a+b+c)<=S and a*b*c<=T:
                count+=1


print(count)
"""

#C
N=int(input())
S=list(map(int,input().split()))
T=list(map(int,input().split()))


for i in range(N):
    T[(i+1)%N] = min(T[(i+1)%N],T[i%N]+S[i%N])

for i in range(N):
    T[(i+1)%N] = min(T[(i+1)%N],T[i%N]+S[i%N])


for ans in T:
    print(ans)

