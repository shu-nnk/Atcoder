#A
N,K,A = map(int,input().split())
getter=A

for i in range(K-1):
    getter+=1
    if getter>N:
        getter=1
print(getter)


#B