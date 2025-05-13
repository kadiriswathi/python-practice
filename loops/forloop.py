for i in range(5):
    print(i)
# for loop with start value and end value it will print 0 to n-1
for i in range(1,7):
    print(i)
# for loop with step count
for i in range(1,10,2):
    print(i)
# for loop with negative step  count
for i in range(5,0,-1):
    print(i)
# number convert into list
number=list(range(1,3))
print(number)
# to print the loop fixed number of times
for i in range(3):
    print(i)
# to access the index elements for the given list
colours=['red','green','blue','yellow']
for i in range(len(colours)):
    print('colour:',colours[i])
#nested loops
for row in range(4):
    for col in range(3):
        print(f'({row},{col})',end='')
    print()
# multipication table
for i in range(1,10):
    for j in range(1,6):
        res=i*j
        print(f"{res:4}",end='')
    print()

    