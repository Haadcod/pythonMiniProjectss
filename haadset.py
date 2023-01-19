#days = set(["mon", "tue", "wed", "thur", "fri", "sat", "sun"])
#months={'jan',"feb","mar"}
#dates={21,22,17}
#days.add("sun")
#days.discard("sun")
#print(days)
#print(months)
#print(dates)
#for d in days:
   # print(d)
daysA =set(["mon","tue","wed"])
daysB =set(["wed","thur","fri","sat","sun"])
alldays =daysA & daysB
alldays =daysA -daysB
print(alldays)