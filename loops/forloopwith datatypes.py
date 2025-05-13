#string datatype iterate based on character
name='swathi'
for c in name:
   print(c)
# for loop with datatypes list iterate the value by value
list=['swathi','venky','gunshika','urvi']
for name in list:
    if name=='swathi':
      
       print(list)
# tuple iterate value by value
coures=('cse','ece','eee','it','mech','civil',41,789,456)
for coure in coures:
    if coure==100: 

     print(coures)
#dictionary datatypes iterate based on key
dict={'name':'swathi','age':30,'dept':'software','sal':50000,'oid':7845}
for i in dict: 
   if dict['age']==30:
   #print(i)# it will print only keys
    print(dict)# it will print total dict

#set datatype iterate based on value by value
temp={'summer','winter','rainy','cold'}
for j in temp:
   print(temp)
# number datatype  is not iterable
no=200
for n in no:
   print(n)




