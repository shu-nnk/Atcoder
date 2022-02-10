#A
X,Y=map(int,input().split())
if Y-X<=0:
    print(0)
elif((Y-X)%10==0):
    print((Y-X)//10)
else:
    print((Y-X)//10+1)

#B
L,R=map(int,input().split())
S=input()
tmp_S=list(S)

hannten=list(reversed(tmp_S[L-1:R]))
new_S=tmp_S[:L-1]+hannten+tmp_S[R:]
print("".join(new_S))


#C









