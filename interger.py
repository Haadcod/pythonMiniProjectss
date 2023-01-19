def add(num):
    if type(num)==int:
        sum=0
        for x in range(num+1):

           sum += x
           return sum
    else:
        return 0
add(5)
