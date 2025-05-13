# without arguments
add=lambda: 2+8
r=add()
print(r)
#with arguments
add=lambda a,b:7+b
r=add(12,23)
print(r)
#with loop
add=lambda a,b:b+10 if a>5 else a-b
print(add(20,7))
