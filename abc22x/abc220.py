#A
"""
A,B,C = map(int,input().split())
temp = -1

for i in range(A,B+1):
    if i%C == 0:
        temp = i
        break

print(temp)
"""

#B
"""
K = int(input())
A,B = map(str,input().split())

#10進数変換

keta_A = len(str(A))
keta_B = len(str(B))

A_10=0
B_10=0
index1=0
index2=0


for i in range(keta_A-1,-1,-1):
    A_10 += K**i * int(A[index1])
    index1 += 1


for j in range(keta_B-1,-1,-1):
    B_10 += K**j * int(B[index2])
    index2 += 1


print(A_10*B_10)
"""


#C
N = int(input())
A = list(map(int,input().split()))
X = int(input())

sum1=0
sum2=0

for i in A:
    sum1+=i
    sum2+=i

count=0
while sum1<X:
    sum1+=sum2
    count+=1
    


temp= sum2*count

count2 = 0
for j in A:
    temp+=j
    if temp<=X:
        count2+=1
    else:
        count2+=1
        break


print(N*count+count2)



    
