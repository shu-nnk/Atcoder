#A
"""
S1=input()
S2=input()
result="Yes"
if S1=="#." and S2==".#":
    result="No"
elif S1==".#" and S2=="#.":
    result="No"

print(result)


#B
A,B = input().split()
A=A[::-1]
B=B[::-1]

min_keta = min(len(A),len(B))
result="Easy"


for i in range(min_keta):
    if int(A[i])+int(B[i])>=10:
        result="Hard"
        break
print(result)

"""

#C
N,W=map(int,input().split())
AB=[]

for i in range(N):
    AB.append(list(map(int,input().split())))


sortedAB=sorted(AB,reverse=True) #美味しさが大きいチーズ順にソート
weightSum=0
oisisaSum=0



for i in sortedAB: #美味しさが大きいチーズから乗せていく
    if weightSum+i[1]<=W:#あるチーズxを全て乗せてもW以下である場合まとめて美味しさ、重さの総数に追加
        weightSum+=i[1]
        oisisaSum+=i[0]*i[1]
    else:#あるチーズ全ての乗せたらWを超過してしまう。1gずつ乗せていく
        for j in range(i[1]):
            weightSum+=1
            if weightSum>W:
                break
            else:
                oisisaSum+=i[0]
        
        else:
            continue

        break

print(oisisaSum)
        

        
        

        



