from functools import reduce
num=[1,3,4,5,6,7]
res=reduce(lambda x,y :x+y,num)
print(res)
rv=reduce(lambda a,b: a+b,[1,3,2,5])
print(rv)