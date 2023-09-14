import os
from itertools import permutations
f='wordlist.txt'
file= open(f,'w')
c = permutations([1,2,3,4,5,6,7,8,9,0],5)
def ts(tup):
    s=''
    for item in tup:
        s=s + str(item)
    return s
for i in c:
    s=ts(i)
    file.write("air@" + s + "\n"+"Air@"+s+"\n")
file.close()
