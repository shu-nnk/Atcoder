import itertools
#A
"""
S = str(input())
t="Hello,World!"

if S==t:
    print("AC")
else:
    print("WA")
"""

#B
'''
N = int(input())

#kは０以上
for i in range(1,4*18+1):
    if 2**i > N:
        print(i-1)
        break
'''

#C
"""
S,K = map(str,input().split())
K = int(K)

dic_S = tuple(S)
dic_S= list(itertools.permutations(dic_S))


list_S=[]

for i in dic_S:
    str = "".join(i)
    list_S.append(str)

list_S = sorted(list(set(list_S)))
print(list_S[K-1])
"""

#D
N,M = map(int,input().split())
l = list(map(int,input().split()))
s=[]

for i in range(1,M+1):
    s.append(i)

def factorize(n):
    a=[]
    while n%2==0:
        a.append(2)
        n//=2
    f=3
    while f*f <=n:
        if n%f==0:
            a.append(f)
            n//=f
        else:
            f+=2
    
    if n!=1:
        a.append(n)
    
    return(a)

t=[]
for j in l:
    t+=factorize(j)

t=list(set(t))
print(t)
print(s)

for i in t:
    for j in s:
        print(f"{j}:{s}")
        
        if j%i==0:
            s.remove(j)
            

print(len(s))
for i in s:
    print(i)




















    





