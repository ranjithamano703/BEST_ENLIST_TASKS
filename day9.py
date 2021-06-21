#program to loop through the list and add +2 to every elements
x=[int(y) for y in input().split()]
for i in range(len(x)):
    x[i]+=2
print(x)
#number pattern
n=int(input("enter a number"))
num=n
for i in range(n):
    for j in range(n-i):
        print(n-j,end=' ')
    print()
#fibonacci series
n=int(input("enter a number"))
a=0
b=1
print(a)
print(b)
for i in range(n-2):
    c=a+b
    a=b
    b=c
    print(c)
#amstrong number
"Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers."
    
n=int(input("enter a number"))
temp=n
sum=0
while(n>0):        
     r=n%10    
     sum=sum+(r*r*r)    
     n=n//10

if(temp==sum):    
     print("armstrong  number ")
else:
     print("not armstrong number") 
#multiplication table of nine
n=int(input("enter a number"))
for i in range(1,n+1):
      ans=9*i
      print("9*{0}={1}".format(i,ans)) 
#positive or negative
n=int(input("enter a number"))
if(n>0):
    print(n,"is positive")
elif(n<0):
    print(n,"is negative")
else:
    print(n,"is zero")
#convert days to age
days=int(input("enter days"))
age=days/365
print(age)
#trignomentry using math function
import math
def trigo(n,m):
    if n=='sin':
       return math.sin(m)
    elif n=='cos':
       return math.cos(m)
    elif n=='cosin':
       return math.cosin(m)
    elif n=='tan':
       return math.tan(m)
    elif n=='cosec':
       return math.cosec(m)
    elif n=='sec':
       return math.sec(m)
x=input()
y=int(input())
result=trigo(x,y)
print(result)
# Python program for simple calculator

# Function to add two numbers
def add(num1, num2):
	return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
	return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
	return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
	return num1 / num2

print("Please select operation -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n")


# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
	print(number_1, "+", number_2, "=",
					add(number_1, number_2))

elif select == 2:
	print(number_1, "-", number_2, "=",
					subtract(number_1, number_2))

elif select == 3:
	print(number_1, "*", number_2, "=",
					multiply(number_1, number_2))

elif select == 4:
	print(number_1, "/", number_2, "=",
					divide(number_1, number_2))
else:
	print("Invalid input")

