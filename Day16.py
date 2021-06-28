def myfunc(n):
  return lambda a:a*n
mydoubler=myfunc(2)
print(mydoubler(11))
#exercise1:create a lambda function that multiplies argument x with argument y
f=lambda x,y:x*y 
print(f(2,4))
#exercise2: create fibonacci series to n using lambda
from functools import reduce
fibo=lambda n :reduce(lambda x,y:x+[x[-1]+x[-2]],range(n-2),[0,1])
print(fibo(5))
#exercise3: program to multiply each number of the given list with given number
lst=[2,3,4,5]
result=list(map(lambda n:n*2,lst))
print(result)
#exercise4: program to find nos divisible by 9 from a list
lst=[12,9,23,27,36,45,56,72,82,90]
result=list(filter(lambda n:n%9==0,lst))
print(result)
#exercise5: program to count even nos in a given lst (int)
lst=[12,9,23,27,36,45,56,72,82,90]
even=list(filter(lambda n:n%2==0,lst))
print(len(even))