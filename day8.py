#merge 2 python dictionaries
def merge(dict1,dict2):
      return(dict2.update(dict1))
dict1={'a':10,'b':20}
dict2={'c':30,'d':40}
print(merge(dict1,dict2))
print(dict2)
#program to sort the value from descending to ascending in the list and convert it to tuple
x=[int(y) for y in input().split()]
x.sort(reverse=True)
print(tuple(x))
#program to list number of items in a dictionary key and sort the list with help of function and without the function
mydict={'team A':[1,2],'team B':[2,3,6],'team C':[4,5,9,8,7],'team D':[2],'team E':[2,4,6,8,10,12]}
length_dict={key: len(value) for key,value in mydict.items()}
print(length_dict)
values=length_dict.values()
values_list=list(values)
print(values_list)
values_list.sort()
print(values_list)
unsorted_list=values_list
sorted_list=[]
while unsorted_list:
    minimum=unsorted_list[0]
    for item in unsorted_list:
        if item<minimum:
            minimum=item
    sorted_list.append(minimum)
    unsorted_list.remove(minimum)
print(sorted_list)
#program to get a string from a given string and change the first occurence of the word to a user specified input
str1= "good morning everyone"
input1=input()
input2=input()
print(str1.replace(input1,input2))
#program to get a string from the given string where all occurences of its first char have changed to capital letter
str1= "good morning everyone hope ur health is good learn good habits from elders"
input1=input()
input2=input1.capitalize()
print(str1.replace(input1,input2))
#program to find reapeated items of list
l=[int(y) for y in input().split()]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')



#program to check the sum of three elements and divided by a value which is given as input by the user
ele1=int(input("enter no1"))
ele2=int(input("enter no2"))
ele3=int(input("enter no3"))
input1=int(input("enter divisor"))
sum=ele1+ele2+ele3
result=sum/input1
print(result)

#program to find the mean,median mode among the three given numbers

# list of elements to calculate mean
n_num = [1, 2, 3, 4, 5]
n = len(n_num)

get_sum = sum(n_num)
mean = get_sum / n

print("Mean / Average is: " + str(mean))


# list of elements to calculate median
n_num = [1, 2, 3, 4, 5]
n = len(n_num)
n_num.sort()

if n % 2 == 0:
	median1 = n_num[n//2]
	median2 = n_num[n//2 - 1]
	median = (median1 + median2)/2
else:
	median = n_num[n//2]
print("Median is: " + str(median))

from collections import Counter

# list of elements to calculate mode
n_num = [1, 2, 3, 4, 5, 5]
n = len(n_num)

data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

if len(mode) == n:
	get_mode = "No mode found"
else:
	get_mode = "Mode is / are: " + ', '.join(map(str, mode))
	
print(get_mode)




#program to swap cases of a given string
s1=input()
s2=input()
print("before swapping {0} {1}:".format(s1,s2))
temp=s2
s2=s1
s1=temp
print("after swapping {0} {1}:".format(s1,s2))
#program to convert an integer to binary&octa decimal
num=int(input("enter an integer no"))
print(bin(num),"in binary")
print(oct(num),"in octal")
print(hex(num),"in hexadecimal")



