>>>x=[int(y) for y in input().split()]
5 10 15 20 25 30 35 40 45 50
>>> del x[3]
>>> print(x)
[5, 10, 15, 25, 30, 35, 40, 45, 50]
>>> x.pop(2)
15
>>> del x[5:7]
>>> print(x)
[5, 10, 25, 30, 35, 50]
>>> a=min(x)
>>> b=max(x)
>>> print("minimum element:",a,"maximum element:",b)
minimum element: 5 maximum element: 50
>>> my_tuple=("bread",25,"butter",30,"milk",30,"egg",65)

>>> def Reverse(tuples):
    new_tup = ()
    for k in reversed(tuples):
        new_tup = new_tup + (k,)
    print(new_tup)

    
>>> Reverse(my_tuple)
(65, 'egg', 30, 'milk', 30, 'butter', 25, 'bread')
>>> >>> my_list=list(my_tuple)
>>> print(my_tuple)
('bread', 25, 'butter', 30, 'milk', 30, 'egg', 65)
>>> print(my_list)
['bread', 25, 'butter', 30, 'milk', 30, 'egg', 65]
>>> 
