def is_even(n):
    return n%2==0
number=[1,2,3,4,5,6]
result=filter(is_even,number)
print(list(result))