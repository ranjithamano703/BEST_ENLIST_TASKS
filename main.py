#1)

print('2'+2)#type error
print(int('xyx'))#ValueError
l=[1,2,3]
print(l[4])#IndexError
print(x)#NameError
print(10/0)#ZeroDivisionError
import maths#ModuleNotFoundError
#SyntaxError
for i in rangerange(10)
  print(i)
#KeyError
d={'a':1,'b':2}
print(d['3'])

#2)a simple calc app
def calculator():
  try:
      print('+')
      print('-')
      print('*')
      print('/')
      print('%')
      print('**')
      operation=input("Select an Operator")
      number1=int(input("enter number1"))
      number2=int(input("enter number2"))
      if operation == '+':
        print(number1+number2)
      elif operation == '-':
        print(number1-number2)
      elif operation == '*':
        print(number1*number2)
      elif operation == '/':
        print(number1/number2)
      elif operation == '%':
        print(nuber1%number2)
      elif operation == '**':
        print(number1**number2)
      else:
        print('invalid operation')
  except Exception as x:
      print(x)
calculator()

#3 print one message if try block raises name NameErro
try:
  print(y)
except NameError:
  print("variable y is not defined")
except :
  print("something else went wrong")

y='hello world'
try:
  print(y)
except NameError:
  print("variable y is not defined")
except :
  print("something else went wrong")
  
  #5 try getting an input inside try catch block
try:
  age=int(input("enter integer value"))
except:
    print("you have entered invalid data type")