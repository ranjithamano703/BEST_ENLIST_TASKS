#importing library
from tkinter import *
from tkinter import ttk

window = Tk()
#Declaring Window Title
window.title("Registration Screen")
#Declaring Window size
window.geometry('600x600')
#Declaring Window Color
window.configure(background = "lightblue");
#below four fields are declared
Firstname = Label(window ,text = "First Name").grid(row = 0,column = 0)
LastName = Label(window ,text = "Last Name").grid(row = 2,column = 0)
Email = Label(window ,text = "Email Id").grid(row = 4,column = 0)
Mobile = Label(window ,text = "Contact Number").grid(row = 6,column = 0)
gender = Label(window ,text = "gender").grid(row = 8,column = 0)

Firstname1 = Entry(window).grid(row = 0,column = 1)
Lastname1 = Entry(window).grid(row = 2,column = 1)
Email1 = Entry(window).grid(row = 4,column = 1)
Mobile1 = Entry(window).grid(row = 6,column = 1)


var=IntVar()
#this creates 'Radio button' widget 
gender=Radiobutton(window,text="Male",padx= 5, variable= var, value=1).grid(row = 8,column = 1)
gender=Radiobutton(window,text="Female",padx= 20, variable= var, value=2).grid(row = 8,column = 2)


label_5=Label(window,text="Country",width=10,font=("bold",10))
label_5.grid(row =10,column = 0)

#this creates list of countries available in the dropdownlist.
list_of_country=[ 'India' ,'US' , 'UK' ,'Germany' ,'Austria']

#the variable 'c' mentioned here holds String Value, by default ""
c=StringVar()
droplist=OptionMenu(window,c, *list_of_country)
droplist.config(width=15)
c.set('Select your Country')
droplist.grid(row =10,column = 1)



# Creating Check Box
#the variable 'var1' mentioned here holds Integer Value, by default 0
var1=IntVar()
#this creates Checkbutton widget 
Checkbutton(window,text="Accept Terms and Condition", variable=var1).grid(row =12,column = 0)



#this creates button for submitting the details provides by the user
Button(window, text='Submit' , width=20,bg="black",fg='white',font=("bold",10)).place(x=70,y=380)



window.mainloop()

