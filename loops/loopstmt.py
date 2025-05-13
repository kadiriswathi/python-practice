names=['swathi','venky','gunshika','urvi']
#with break stmt
for i in names:
    print(i)
    if i=='venky':
        print('name is:',names)
        break
#with continue
l=[3,5,12,6,7,88,4,23]
for j in l:
    print(j)
    if j<= 10:
        continue
    print(j)