import sys
s=[]

for l in sys.stdin:
    s.append(str(l).rstrip("\n"))



for i in range(97,97+26):
    count=0
    for j in range(len(s)):
        for k in range(len(s[j])):
            if chr(i)==s[j][k].lower():
                count+=1
    
    print(f"{chr(i)} : {count}")
