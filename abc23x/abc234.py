#A
t=int(input())

def function(num):
    result= (num**2)+2*num+3
    return result

ans = function(function(function(t)+t) + function(function(t)))
print(ans)

#B
import math
N=int(input())
tmp=0
max_length=0

point_list=[list(map(int, input().split())) for l in range(N)]

for i in range(N-1):
    for j in range(i+1,N):
        tmp= (point_list[i][0]-point_list[j][0])**2 + (point_list[i][1]-point_list[j][1])**2
        length=math.sqrt(tmp)

        if length>max_length:
            max_length=length

print(max_length)


#C
def dec2bin(target):
    amari=[]
    while target!=0:
        amari.append(str(target%2))
        target = target//2
    
    amari.reverse()
    return amari
  
K=int(input())
two_num="".join(dec2bin(K))
result=two_num.replace("1","2")

print(result)