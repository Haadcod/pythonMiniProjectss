import collections

dict1= {'day1':'mon','day2':'tue'}
dict2= {'day3':'wed','day4':'thur'}
res = collections.ChainMap(dict1,dict2)
print(res.maps,'\n')