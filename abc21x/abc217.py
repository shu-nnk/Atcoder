#A
"""
S,T = map(str,input().split())

if S<T:
    print("Yes")
else:
    print("No")
"""

#B
"""
S=["ABC","ARC","AGC","AHC"]
for i in range(3):
    t = str(input())
    S.remove(t)

print(S[0])
"""

#C
"""
N = int(input())
p = list(map(int,input().split()))
q=[]

for k in range(N):
    q.append(0)



for i in range(N):
    q[p[i]-1] = i+1
    

print(" ".join(map(str,q)))
"""






#D
L,Q = map(int,input().split())
tree1=[]
tree2=[]

for i in range(1,L):
    tree1.append(str(i))


tree2.append(tree1)
queri = []
for i in range(Q):
    s = list(map(str,input().split()))
    queri.append(s)

#print(queri)
#print(tree2)
for i in queri:
    if i[0]=="2":
        for j in tree2:
            if str(i[1]) in j:
                print(len(j)+1)
    else:
        for j in tree2:
            if str(i[1]) in j:
                index=j.index(i[1])
                temp1 = j[:index]
                temp2 = j[index+1:]

                #print(tree)

                tree2.pop(tree2.index(j))
                tree2.append(temp1)
                tree2.append(temp2)






    





