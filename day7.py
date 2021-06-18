def myFun(num): 
     num[0] = 20
list1 = [1, 2, 3, 4, 5]  
myFun(list1)
print(list1)
def my_function():
  print("Hello from a function")

my_function()
def csk(fname):#fname---->parameter
  print("Player name is" + fname)

csk("Dhoni")#argument
csk("Raina")
csk("Sam")
def ipl(csk_cap,rcb_cap):
  print(csk_cap +" VS "+ rcb_cap)

ipl("Dhoni","Kohli")
def my_function(*team):
  print("The youngest member is " + team[0])

my_function("sam", "tom", "ben")
def my_function(child3, child2, child1):
  print("The youngest child is " + child1)

my_function(child1 = "Sam", child2 = "Ben", child3 = "Tom")
def my_function(x):
  return 5 * x

print(my_function(3))
def csk(fname = "Dhoni"):
  print("Captain for CSK is " + fname)

csk()
#exercise 1
def add(x,y):
  value=x+y
  print("Addition of two numbers is ",value)
def sub(p,q):
  value=p-q
  print("Subtraction of two numbers is ",value)
def mul(r,s):
  value=r*s
  print("Division of two numbers is ",value)
def div(t,u):
   value=t/u
   print("Multiplication of two numbers is ",value)
a=int(input("enter a number"))
b=int(input("enter a number"))
add(a,b)
sub(a,b)
mul(a,b)
div(a,b)
#Exercise 2
def covid(patient_name,body_temperature="98degree"):
  print("patient name:",patient_name)
  print("body temp:",body_temperature)

covid("kaviya")
covid("ramya","110degree")













