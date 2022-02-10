#A
S=input()
a,b=map(int,input().split())
tmp=list(S)
tmp[a-1]=S[b-1]
tmp[b-1]=S[a-1]
print("".join(tmp))

#B
N=int(input())
A=list(map(int,input().split()))
num=[]

for _ in range(N):
    num.append(0)

for a in A:
    num[a-1]+=1

for i in range(N):
    if num[i]!=4:
        print(i+1)

#C
N,M=map(int,input().split())
S=list(map(str,input().split()))
T=list(map(str,input().split()))

for s in S:
    print("Yes" if s in T else "No")

#D



