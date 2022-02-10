#A
"""
A,B = map(int,input().split())
sub = A-B
print(32**sub)
"""

#B
"""
import copy
S = input()
T = input()

list_S = list(S)
list_S2 = list(S)
result = "No"



for i in range(len(S)-1):
    list_S = copy.copy(list_S2)
    temp = list_S[i]
    list_S[i] = list_S[i+1]
    list_S[i+1] = temp


    if list_S == list(T):
        result="Yes"
        break

if list_S2 == list(T):
    result = "Yes"

print(result)
"""


#C

N = list(input())

sortedNum = sorted(N,reverse=True)
num1=[]
num2=[]

count=1

for i in sortedNum:
    if count%2==1:
        num1.append(i)
    else



