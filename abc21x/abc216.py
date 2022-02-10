#A
"""""
x,y=map(int,input().split("."))

if y<=2:
    print(f"{x}-")
elif y>=3 and y<=6:
    print(x)
else:
    print(f"{x}+")
"""""

#B
"""""
N = int(input())
L = []
flag=False

for i in range(N):
    S,T=map(str,input().split())
    L.append([S,T])


for i in range(N):
    if i==N-1:
        print("No")
        break
    for j in range(i+1,N):
        if (L[i][0]==L[j][0]) and (L[i][1]==L[j][1]):
            print("Yes")
            flag=True
            break
    if flag==True:
        break
"""

#C
N=int(input())
s=""

while N>=1:
    if(N%2==0):
        N=N/2
        s=s+"B"
    else:
        N=N-1
        s=s+"A"

L = reversed(list(s))
new_s =''.join(L)


print(new_s)







