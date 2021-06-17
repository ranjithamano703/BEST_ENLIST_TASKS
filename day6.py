#merge two dictionaries
def merge(dict1,dict2):
      return(dict2.update(dict1))
dict1={'a':10,'b':20}
dict2={'c':30,'d':40}
print(merge(dict1,dict2))
print(dict2)
#remove a key from dictionary
dict1={'a':10,'b':20}
del dict1['a']
print(dict1)
#map two lists into a dictionary
keys=[]
values=[]
n=int(input("enter no of elements for dictionary:"))
print("for keys:")
for i in range(0,n):
    element=int(input("enter element {}:".format(i)))
    keys.append(element)
print("for values:")
for i in range(0,n):
    element=int(input("enter element {}:".format(i)))
    values.append(element)
d=dict(zip(keys,values))
print("the dictionary is:")
print(d)
#length of a set
a={1,2,3,4,5,6,2}
print("the length of set is:",len(a))
#to remove intersection of 2ndset from 1stset
x={1,2,3,4,5}
y={4,5,6,7,8}
x=x-y
print(x)
print(y)
