#A
"""
N = int(input())
S = list(map(str, input().split()))

if S[N-1]=="o":
    print("Yes")
else:
    print("No")
"""

#B
"""
P = list(map(int,input().split(" ")))
S=[]

for i in P:
    S.append(chr(96+i))

print("".join(S))
"""

#C
"""
import numpy as np
import itertools
import re

N = int(input())

#print("S")
S=[list(map(str,input())) for S in range(N)]
#print(S)
#print("T")
T=[list(map(str,input().split())) for T in range(N)]

T = itertools.chain.from_iterable(T)
T = "".join(T)

pattern = re.findall("#.*#",T)
pattern = "".join(pattern)


S_90 = np.rot90(S)
#print(S_90)
S_180 = np.rot90(S_90)
S_270 = np.rot90(S_180)

S_90 = "".join(itertools.chain.from_iterable(S_90))
S_180 = "".join(itertools.chain.from_iterable(S_180))
S_270 = "".join(itertools.chain.from_iterable(S_270))

#print(S_90)
#print(type(S_90))


if (pattern in S_90) or (pattern in S_180) or (pattern in S_270):
    print("Yes")
else:
    print("No")
"""










 
