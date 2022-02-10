#A
S=list(input())
set_S = set(S)

if len(set_S)==3:
    print(6)
elif len(set_S)==2:
    print(3)
else:
    print(1)


#B
"""
N=int(input())
l = [list(map(int, input().split())) for l in range(1,N)]
result="No"

AllNum=[0 for i in range(N)]


for j in l:
    AllNum[j[0]-1] = AllNum[j[0]-1]+1
    AllNum[j[1]-1] = AllNum[j[1]-1]+1


for k in AllNum:
    if k==N-1:
        result="Yes"
        break
print(result)
"""

#C
