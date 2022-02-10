n = int(input())
scoreT=0
scoreH=0
for i in range(n):
    cardT, cardH = map(str,input().split())
    if cardT>cardH:
        scoreT+=3
    elif cardT==cardH:
        scoreT+=1
        scoreH+=1
    else:
        scoreH+=3


print(f"{scoreH} {scoreT}")


