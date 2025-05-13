def add(a):
    return  a + 10

mo = map(add,(1,2,3,4,5,6))
print(list(mo))
#with lambda
mo=map(lambda a,b:a+b,(1,2,3,4,5,6,7),(10,30,20))
print(tuple(mo))