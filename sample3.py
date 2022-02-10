import sys
print("aaa")
W = str(input()).lower()
T =[]
count=0

while True:
    t=str(input())
    if t=="END_OF_TXT":
        break
    T+= t.lower().split()
    

for i in T:
    if i==W:
        count+=1

print(T)
print(W)


print(count)







