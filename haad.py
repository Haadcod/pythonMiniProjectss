from array import *
T=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
T.insert(2,[0,5,11,13,6])
del T[3]
del T[2]
#print(T[0])
#print(T[1][2])
for r in T:
    for c in r:
        print(c,end=" ")
    print()
