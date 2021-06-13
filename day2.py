#how to print a value?
print("30 days 30 hour challenge")
print('30 days 30 hour challenge')
#does not matter you use single or double qoutes

#Assinging String to Variable
hours="Thirty"
print(hours)
#indexing using String
Days="Thirty Days"
print(Days[0])
print(Days[-1])
print(Days[7])
print(Days[8])
#how to print a particular character from certain text?
challenge="I WILL WIN"
print(challenge[7:10])
#print length of the character
print(len(challenge))
#convert string into lower character
print(challenge.lower())
#string conctenation- joining two strings
a="30 days"
b="30 hours"
c=a+b
print(c)
#Adding space during concatenation
c=a+" "+b
print(c)
#casefold usage
text="Thirty days and Thirty hours"
x=text.casefold()
print(x)
text="DON'T TROUBLE UNTIL TROUBLE TROUBLES YOU"
x=text.casefold()
print(x)
x=text.capitalize()
print(x)
x=text.find("UNTIL")
print(x)
x=text.find("TROUBLE")
print(x)
x=text.isalpha()
print(x)
x=text.isalnum()
print(x)

