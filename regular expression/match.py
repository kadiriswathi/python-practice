import re
name='swathi'
#match it will the starting postion
abc=re.match('swa',name)
print(abc.group())


name = 'sriram'

mo = re.match('sri', name)
print(mo.group())
