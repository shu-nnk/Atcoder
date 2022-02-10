#A
"""
S,T,X= map(int,input().split())
result="No"
if S<T:
    if S<=X and X<T:
        result="Yes"
else:
    if S<=X or X<T:
        result="Yes"
print(result)
"""

#B
"""
N,X = map(int,input().split())
A = list(map(int,input().split()))

judge =[]
for i in range(N): #友人iが既に秘密を知っているか
    judge.append("No")

count=0

while judge[X-1]=="No":
    judge[X-1]="Yes"
    X=A[X-1]
    count+=1

print(count)
"""
#C
""""
from numpy.lib.function_base import copy
from scipy.stats import rankdata
import copy
N,K = map(int,input().split())
P=[]
scoreList=[]
for i in range(N):
    P.append(list(map(int,input().split())))

for j in P:
    sum=0
    for k in j:
        sum+=k
    scoreList.append(sum)

print(scoreList)

for a in range(N):
    temp=copy.copy(scoreList)
    temp[a] = temp[a] +300

    asc = rankdata(temp)
    desc= (len(asc) - asc + 1).astype(int)


    if desc[a] <= K:
        print("Yes")
    else:
        print("No")

N,K = map(int,input().split())
P=[]
score=[]
for i in range(N):
    P.append(list(map(int,input().split())))

for j in P:
    sum=0
    for k in j:
        sum+=k
    score.append(sum)

sorted_score = sorted(score,reverse=True)

for x in score:
    if x+300>=sorted_score[K-1]:
        print("Yes")
    else:
        print("No")
"""
















    



