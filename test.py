def combination():


    n, x = map(int,input().split())

    if n==0 and x==0:
        return

    count = 0

    for i in range(1,n+1):
        for j in range(1,n+1):
            if i>=j:
                continue
            k=x-(i+j)
            if k<=n and k>j:
                count+=1
            
    print(count)
    combination()



combination()

