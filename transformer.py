from math import sin,cos, pi,sqrt
while True:
    n = int(input())
    if n==0:
        break
    sum=0
    s = list(map(int,input().split()))
    for i in s:
        sum+=i
    m=sum/n

    sum2=0
    for j in s:
        sum2+=(j-m)*(j-m)/n

    alpha=sqrt(sum2)
    print(alpha)





