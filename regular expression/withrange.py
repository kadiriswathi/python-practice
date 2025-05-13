import re
name='swathi'
mo=re.match('\w{3,6}',name)
print(mo.group())
