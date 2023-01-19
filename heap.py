import heapq
H=[23,43,23,12,67,1,4,6,89,0]
heapq.heapify(H)
print(H)
heapq.heappush(H,45)
print(H)
heapq.heappop(H)
print(H)
heapq.heapreplace(H,21)
print(H)
