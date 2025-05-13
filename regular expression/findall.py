import re

s = '345sri89ram99yes9678'

v = re.search('\d+', s)
print(' SEARCH  :', v.group())


