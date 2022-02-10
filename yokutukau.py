
#join
s = ','.join(l)

#順列
from audioop import reverse
from hashlib import new
import itertools
from turtle import right
for v in itertools.permutations(l,4):
    print(v)
    

#bisect_left
from typing import List
def bisect_left(arr: List[int], target:int, left:int, rigth:int):
    while left<right:
        mid=(left+right)//2
        if arr[mid]>=target:
            right=mid
        else:
            left=mid+1
    return left


import bisect
left_index=bisect.bisect_left(List,target)


#スライス
mylist=["a","b","c","d"]
mylist[1:4]
-->#["b","c","d"]
mylist[3:4]
-->#["D"]
mylist[2:]
-->#["c","d"]
mylist[:3]
-->#["a","b","c"]


#reverse
l=[1,2,3,4,5]
new_l=list(reversed(l))
l.reverse()

