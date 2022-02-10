#A
"""
X= int(input())
result="No"

if X%100==0 and X>=100:
    result="Yes"

print(result)
"""

#B
"""
S=input()
S2=S
S_min=S
S_max=S
check=True

while(True):
    S2=S2+S2[0]
    S2=S2.replace(S2[0],"",1)
    

    if S2==S:
        break

    if S_min>S2:
        S_min = S2
    
    if S_max<S2:
        S_max = S2


print(S_min)
print(S_max)
"""

#C
N=int(input())
l = [list(map(int, input().split())) for l in range(N)]

print("start")

sumLine=0
for i in l:
    sumLine=sumLine+i[0]

L_num=0
R_num=-1
L_line=l[L_num][0]
L_speed=l[L_num][1]
L_length=0

R_line=l[R_num][0]
R_speed=l[R_num][1]
R_length=0

time=0.00001


while(True):
    print("aaa")
    L_length=L_length+L_speed*time
    R_length=R_length+R_speed*time

    if L_length+R_length==sumLine:
        break

    if L_length==L_line:
        L_num=L_num+1
    
    if R_length==R_line:
        R_num=R_num-1



print(L_length)
