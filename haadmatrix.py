from numpy import *
a = array([['mon',18,20,22,17,],['tue',11,18,21,18],
           ['wed',15,21,20,19],['thur',11,20,22,21],
           ['fri',18,17,23,22],['sat',12,22,20,18],
           ['sun',13,15,19,16]])
#m= reshape(a,(7,5))
m_r=append(a,[['avg',12,15,13,11]],0)
m_c= insert(a,[5],[[1],[2],[3],[4],[5],[6],[7],1])
print(m_c)
print(m_r)
print(a)
for r in a:
   for c in r:
        print(c,end=" ")
   print()
print(a[2])
print(a[4][3])