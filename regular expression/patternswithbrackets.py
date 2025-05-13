import re
name='Swathi'
ro=re.match('[sS]wathi',name)
print(ro.group())
name="swathi"
mo=re.match('[a-z]wathi',name)
print(mo.group())
mo = re.match('[a-z]riram', 'kumar')
print(mo.group())
mo = re.match('[A-E]riram', 'Eriram')
print(mo.group())