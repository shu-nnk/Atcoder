#A
N=int(input())

if 1<=N and N<10:
    print("AGC"+"00"+str(N))
elif 10<=N and N<=41:
    print("AGC"+"0"+str(N))
else:
    print("AGC"+"0"+str(N+1))

