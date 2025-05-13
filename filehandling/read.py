fh=open(r'C:\python practice\filehandling\name.txt','r')
print(fh.read())
print(' 1 :: ', fh.readline())

print(' 2 :: ', fh.readline())


## Using readlines we can read total lines in a file and  return in list format
print(' READ LINES 1 ', fh.readlines())
fh.close()