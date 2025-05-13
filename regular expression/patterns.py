import re
name='swathi'
r=re.search('\w+',name)
print(r.group())
name="gunshika123"
r=re.search('\w*',name)
print(r.group())
name = 'sri*123'
mo = re.search('sri\*123', name)
print(mo.group())
